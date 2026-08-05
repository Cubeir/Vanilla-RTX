#!/usr/bin/env python3
"""
pack_builder.py — drop-in Minecraft Bedrock resource pack builder + releaser.

Lives right next to the workflow that runs it (.github/workflows/) so the
entire tool is two files in one folder - copy that folder into any repo
that hosts Bedrock resource packs and it works with zero code changes.

What it does, in order:
  1. Decides whether a real rebuild is warranted: compares header.version
     in every (non-excluded) manifest.json touched by this push against
     its previous committed value (git diff BEFORE_SHA vs AFTER_SHA). Any
     inequality counts - a version going down (e.g. reverting a mistake)
     triggers a build exactly the same as going up. A file being merely
     *touched* (e.g. a description edit) does NOT count. No state file
     anywhere; git history is the only source of truth. FORCE=true (manual
     workflow_dispatch runs) always builds, skipping this check.
  2. If a rebuild is warranted: every manifest.json anywhere in the repo
     is discovered on its own (no folder list to maintain), except any
     path under EXCLUDE_PATHS, which is ignored completely - not built,
     not watched for version changes, as if it doesn't exist. Each pack
     is zipped as <folder-name>-<version>.mcpack - the contents of the
     folder containing that manifest, flattened (no wrapper directory in
     the zip). An "__enhancements" folder (name configurable) next to a
     manifest, if present, is merged into that pack before zipping,
     unconditionally. Anything named with a leading "__" is treated as
     tooling/notes and never shipped, except __enhancements' own contents,
     which are deliberately merged in.
  3. If more than one pack was built, all of them are also bundled into
     <BUNDLE_NAME_PREFIX>-<year>.<month>.<day>.mcaddon (just a zip of the
     individual .mcpacks). Exactly one pack -> no bundle. If this runs more
     than once on the same date, the workflow deletes the previous same-day
     release before recreating it, so the filename is always just the date -
     no counter needed to keep same-day rebuilds from colliding.
  4. Release notes are written listing every pack + version in this build,
     what changed since the last build, a Full Changelog compare link
     (computed from git tags directly - no reliance on GitHub's built-in
     release-notes generator, so it lands exactly where we put it instead
     of always being appended at the very end), and an optional static
     footer.

Env vars (all optional, set by the workflow):
  BEFORE_SHA             commit SHA before the push (github.event.before)
  AFTER_SHA              commit SHA after the push (github.event.after)
  FORCE                  "true" to always build, skipping the version check
  ENHANCEMENTS_DIR_NAME  default "__enhancements"
  BUNDLE_NAME_PREFIX     default "All-Packs" - the date/build number is
                         always appended regardless of what this is set to
  EXCLUDE_PATHS          comma-separated repo-relative folder paths to
                         ignore completely, subfolders included, e.g.
                         "Ye-Olde-Resonator,Some/Nested/Folder". Empty by
                         default (nothing excluded).
  RELEASE_NOTES_FOOTER   optional static text appended to the end of every
                         release's notes (e.g. install instructions, a
                         support link). Empty by default.
"""
import json
import os
import re
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ZERO_SHA = "0" * 40
JUNK_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}
DATE_TAG_RE = re.compile(r"^release-\d{4}-\d{2}-\d{2}$")

ENHANCEMENTS_DIR_NAME = os.environ.get("ENHANCEMENTS_DIR_NAME", "__enhancements")
BUNDLE_NAME_PREFIX = os.environ.get("BUNDLE_NAME_PREFIX", "All-Packs")
RELEASE_NOTES_FOOTER = os.environ.get("RELEASE_NOTES_FOOTER", "").strip()

EXCLUDE_PREFIXES = [
    tuple(PurePosixPath(p.strip()).parts)
    for p in os.environ.get("EXCLUDE_PATHS", "").split(",")
    if p.strip()
]

NOW = datetime.now(timezone.utc)


def git(*args, cwd=None):
    result = subprocess.run(["git", *args], capture_output=True, text=True, cwd=cwd)
    return result.stdout if result.returncode == 0 else None


def repo_root() -> Path:
    out = git("rev-parse", "--show-toplevel")
    return Path(out.strip()) if out else Path.cwd()


def set_output(name: str, value: str):
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"{name}={value}\n")
    else:
        print(f"[output] {name}={value}")


def is_dunder(name: str) -> bool:
    return name.startswith("__")


def is_excluded(rel_parts: tuple) -> bool:
    return any(rel_parts[: len(prefix)] == prefix for prefix in EXCLUDE_PREFIXES)


def repo_slug(root: Path):
    env_repo = os.environ.get("GITHUB_REPOSITORY")
    if env_repo:
        return env_repo
    url = git("remote", "get-url", "origin", cwd=root)
    if not url:
        return None
    url = url.strip()
    if url.endswith(".git"):
        url = url[: -len(".git")]
    if url.startswith("git@"):
        parts = url.split(":", 1)
        return parts[1] if len(parts) == 2 else None
    if "github.com/" in url:
        return url.split("github.com/", 1)[1]
    return None


def build_full_changelog_line(root: Path, current_tag: str) -> str:
    """Compares current_tag against the most recent *other* existing
    release-* tag, so it works out to the right thing even when this is a
    same-day rebuild replacing an earlier tag with the same date."""
    repo = repo_slug(root)
    if not repo:
        return ""
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")

    tags_out = git("tag", "--list", "release-*", "--sort=-refname", cwd=root) or ""
    prev_tag = next(
        (t.strip() for t in tags_out.splitlines() if DATE_TAG_RE.match(t.strip()) and t.strip() != current_tag),
        None,
    )

    if prev_tag:
        return f"**Full Changelog**: [{prev_tag}...{current_tag}]({server}/{repo}/compare/{prev_tag}...{current_tag})"
    return f"**Full Changelog**: {server}/{repo}/commits/{current_tag}"


def extract_version(text):
    if not text:
        return None
    try:
        data = json.loads(text)
        return ".".join(str(p) for p in data["header"]["version"])
    except Exception:
        return None


# --------------------------- step 1: should we build? ---------------------------

def compute_changes(root: Path):
    """Returns (should_build: bool, changes: list[(label, old, new)], note: str)."""
    if os.environ.get("FORCE", "false").lower() == "true":
        return True, [], "Manually triggered build - no version comparison was performed."

    before = os.environ.get("BEFORE_SHA", "")
    after = os.environ.get("AFTER_SHA", "")

    if not before or before == ZERO_SHA:
        return True, [], "Initial build - no prior version history to compare against."

    diff = git("diff", "--name-only", before, after, cwd=root)
    if diff is None:
        return True, [], "Could not diff commits - built to be safe."

    manifest_paths = [p for p in diff.splitlines() if p.endswith("manifest.json")]
    manifest_paths = [p for p in manifest_paths if not is_excluded(PurePosixPath(p).parts[:-1])]
    if not manifest_paths:
        return False, [], "This push didn't touch any (non-excluded) manifest.json."

    changed = []
    for path in manifest_paths:
        old_version = extract_version(git("show", f"{before}:{path}", cwd=root))
        full_path = root / path
        new_version = extract_version(full_path.read_text(encoding="utf-8")) if full_path.exists() else None
        if old_version != new_version:
            label = PurePosixPath(path).parent.name
            changed.append((label, old_version, new_version))

    if changed:
        return True, changed, ""
    return False, [], "manifest.json touched, but header.version didn't actually change."


# --------------------------- step 2: build ---------------------------

def find_packs(root: Path):
    roots = []
    for manifest_path in sorted(root.rglob("manifest.json")):
        parts = manifest_path.relative_to(root).parts
        if ".git" in parts or ENHANCEMENTS_DIR_NAME in parts:
            continue
        if is_excluded(parts[:-1]):
            continue
        roots.append(manifest_path.parent)

    name_counts = {}
    for r in roots:
        name_counts[r.name] = name_counts.get(r.name, 0) + 1

    packs = []
    for r in roots:
        if name_counts[r.name] > 1:
            pack_id = "-".join(r.relative_to(root).parts)  # disambiguate collisions
        else:
            pack_id = r.name
        packs.append((pack_id, r))
    return packs


def copy_filtered(src: Path, dst: Path, skip_dirs=()):
    """Recursively copy src -> dst, skipping dunder-prefixed entries, named
    skip_dirs, and common OS junk files. Overwrites files already in dst."""
    for r, dirs, files in os.walk(src):
        r_path = Path(r)
        dirs[:] = [d for d in dirs if not is_dunder(d) and d not in skip_dirs]
        target_dir = dst / r_path.relative_to(src)
        target_dir.mkdir(parents=True, exist_ok=True)
        for f in files:
            if is_dunder(f) or f in JUNK_FILES:
                continue
            shutil.copy2(r_path / f, target_dir / f)


def zip_dir_contents(src: Path, zip_path: Path):
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for r, _, files in os.walk(src):
            for f in files:
                fp = Path(r) / f
                zf.write(fp, fp.relative_to(src))


def build_pack(pack_id: str, pack_root: Path, version: str, dist_dir: Path, work_dir: Path) -> Path:
    build_dir = work_dir / pack_id
    copy_filtered(pack_root, build_dir, skip_dirs=(ENHANCEMENTS_DIR_NAME,))

    enh_dir = pack_root / ENHANCEMENTS_DIR_NAME
    if enh_dir.is_dir():
        copy_filtered(enh_dir, build_dir)  # merge, overwrites on conflict

    zip_path = dist_dir / f"{pack_id}-{version}.mcpack"
    zip_dir_contents(build_dir, zip_path)
    return zip_path


def build_bundle(mcpack_paths, dist_dir: Path) -> Path:
    date_part = f"{NOW.year}.{NOW.month}.{NOW.day}"
    bundle_path = dist_dir / f"{BUNDLE_NAME_PREFIX}-{date_part}.mcaddon"
    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(mcpack_paths):
            zf.write(p, p.name)
    return bundle_path


def write_release_notes(root: Path, built: dict, changes: list, note: str, full_changelog_line: str):
    lines = [f"## Packs in this build ({len(built)})", ""]
    for pack_id in sorted(built):
        _, version = built[pack_id]
        lines.append(f"- **{pack_id}** — {version}")

    lines += ["", "## Version changes since last build", ""]
    if changes:
        for label, old, new in changes:
            lines.append(f"- **{label}**: `{old or '(new pack)'}` → `{new or '(removed)'}`")
    else:
        lines.append(f"_{note}_")

    if full_changelog_line:
        lines += ["", full_changelog_line]

    if RELEASE_NOTES_FOOTER:
        lines += ["", "---", "", RELEASE_NOTES_FOOTER]

    (root / "RELEASE_NOTES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_everything(root: Path, changes: list, note: str):
    dist_dir = root / "dist"
    work_dir = root / ".build-tmp"
    for d in (dist_dir, work_dir):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    packs = find_packs(root)
    if not packs:
        print("No manifest.json files found (after exclusions) -- nothing to build.")
        set_output("pack_count", "0")
        return

    print(f"Found {len(packs)} pack(s):")
    built = {}
    for pack_id, pack_root in packs:
        version = extract_version((pack_root / "manifest.json").read_text(encoding="utf-8")) or "unknown"
        has_enh = (pack_root / ENHANCEMENTS_DIR_NAME).is_dir()
        print(f"  {pack_id} (v{version}){' [enhancements merged]' if has_enh else ''}")
        built[pack_id] = (build_pack(pack_id, pack_root, version, dist_dir, work_dir), version)

    if len(built) > 1:
        bundle_path = build_bundle([p for p, _ in built.values()], dist_dir)
        print(f"\nBundled all {len(built)} packs into {bundle_path.name}")

    current_tag = f"release-{NOW.strftime('%Y-%m-%d')}"
    full_changelog_line = build_full_changelog_line(root, current_tag)
    write_release_notes(root, built, changes, note, full_changelog_line)

    shutil.rmtree(work_dir, ignore_errors=True)
    set_output("pack_count", str(len(built)))
    print(f"\nBuilt {len(built)} pack(s) into {dist_dir}")


def main():
    root = repo_root()

    set_output("iso_date", NOW.strftime("%Y-%m-%d"))
    set_output("human_date", f"{NOW.day} {NOW.strftime('%B')} {NOW.year}")

    do_build, changes, note = compute_changes(root)
    if note:
        print(note)
    set_output("should_build", "true" if do_build else "false")

    if not do_build:
        set_output("pack_count", "0")
        return

    build_everything(root, changes, note)


if __name__ == "__main__":
    main()
