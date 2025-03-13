@echo off
set "file=%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt"

REM Read options.txt and modify graphics_mode to ray tracing
(for /f "tokens=1,* delims=:" %%A in ('type "%file%"') do (
    if /i "%%A"=="graphics_mode" (
        echo graphics_mode:3
    ) else (
        echo %%A:%%B
    )
)) > "%file%.tmp"

REM Save changes
move /y "%file%.tmp" "%file%"

REM Delay for a few milliseconds just in case
ping -n 2 127.0.0.1 >nul

REM Launch Minecraft
start minecraft://