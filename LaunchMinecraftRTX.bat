@echo off
setlocal enabledelayedexpansion

:MAIN
cls
echo ================================
echo   Launch Minecraft with RTX
echo ================================

REM Default paths, change if your options.txt files are located elsewhere
set "mc_file=%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt"
set "mc_preview_file=%LOCALAPPDATA%\Packages\Microsoft.MinecraftWindowsBeta_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt"

call :CHECK_RTX_STATUS
call :CHECK_VSYNC_STATUS

echo [1] Minecraft            %mc_rtx_status%
echo [2] Minecraft Preview    %mc_preview_rtx_status%
echo [3] %vsync_status%
echo [0] Exit
echo.
choice /c 1230 /n /m "Select an option [1/2/3/0]:"

if errorlevel 4 (
    exit /b
) else if errorlevel 3 (
    call :TOGGLE_VSYNC
    goto MAIN
) else if errorlevel 2 (
    call :ENABLE_RTX "preview"
    goto MAIN
) else if errorlevel 1 (
    call :ENABLE_RTX "regular"
    goto MAIN
)

goto MAIN

:CHECK_RTX_STATUS

set "mc_rtx_status=Status: Unknown"
if exist "%mc_file%" (
    for /f "tokens=1,* delims=:" %%A in ('type "%mc_file%"') do (
        if /i "%%A"=="graphics_mode" (
            if "%%B"=="3" (
                set "mc_rtx_status=Status: Enabled"
            ) else (
                set "mc_rtx_status=Status: Disabled"
            )
        )
    )
) else (
    set "mc_rtx_status=Status: File not found"
)

set "mc_preview_rtx_status=Status: Unknown"
if exist "%mc_preview_file%" (
    for /f "tokens=1,* delims=:" %%A in ('type "%mc_preview_file%"') do (
        if /i "%%A"=="graphics_mode" (
            if "%%B"=="3" (
                set "mc_preview_rtx_status=Status: Enabled"
            ) else (
                set "mc_preview_rtx_status=Status: Disabled"
            )
        )
    )
) else (
    set "mc_preview_rtx_status=Status: File not found"
)
exit /b

:CHECK_VSYNC_STATUS

set "mc_vsync=unknown"
set "mc_preview_vsync=unknown"

if exist "%mc_file%" (
    for /f "tokens=1,* delims=:" %%A in ('type "%mc_file%"') do (
        if /i "%%A"=="gfx_vsync" (
            if "%%B"=="0" (
                set "mc_vsync=disabled"
            ) else (
                set "mc_vsync=enabled"
            )
        )
    )
)

if exist "%mc_preview_file%" (
    for /f "tokens=1,* delims=:" %%A in ('type "%mc_preview_file%"') do (
        if /i "%%A"=="gfx_vsync" (
            if "%%B"=="0" (
                set "mc_preview_vsync=disabled"
            ) else (
                set "mc_preview_vsync=enabled"
            )
        )
    )
)

if "%mc_vsync%"=="enabled" (
    if "%mc_preview_vsync%"=="enabled" (
        set "vsync_status=Disable VSync        Status: Enabled (Recommended to Disable)"
    ) else (
        set "vsync_status=Disable VSync        Status: Enabled for Minecraft (Recommended to Disable)"
    )
) else (
    if "%mc_preview_vsync%"=="enabled" (
        set "vsync_status=Disable VSync        Status: Enabled for Minecraft Preview (Recommended to Disable)"
    ) else (
        set "vsync_status=Disable VSync        Status: Disabled (You can still enable VSync via your graphics card's control panel)"
    )
)
exit /b

:ENABLE_RTX
REM MC launch protocol based on input
if "%~1"=="preview" (
    set "file=%mc_preview_file%"
    set "protocol=minecraft-preview://"
    set "version_name=Minecraft Preview"
) else (
    set "file=%mc_file%"
    set "protocol=minecraft://"
    set "version_name=Minecraft"
)


if not exist "!file!" (
    echo.
    echo Error: Options file for %version_name% not found.
    echo Make sure the game is installed and has been launched at least once, or manually set file paths by editing the script.
    echo.
    pause
    exit /b
)

REM read-only attribute
attrib -r "!file!" >nul 2>&1

REM Updates graphics_mode
echo.
echo Enabling ray tracing for %version_name%...
(for /f "tokens=1,* delims=:" %%A in ('type "!file!"') do (
    if /i "%%A"=="graphics_mode" (
        echo graphics_mode:3
    ) else (
        echo %%A:%%B
    )
)) > "!file!.tmp"
move /y "!file!.tmp" "!file!" >nul

echo Ray tracing enabled for %version_name%.
echo Launching %version_name%...
start "" "%protocol%"
echo.
echo %version_name% launched. Returning to menu...
exit

:TOGGLE_VSYNC

REM Disable VSync for both versions if they exist
if exist "%mc_file%" (
    echo.
    echo Disabling VSync for Minecraft...
    
    attrib -r "%mc_file%" >nul 2>&1
    
    (for /f "tokens=1,* delims=:" %%A in ('type "%mc_file%"') do (
        if /i "%%A"=="gfx_vsync" (
            echo gfx_vsync:0
        ) else (
            echo %%A:%%B
        )
    )) > "%mc_file%.tmp"
    move /y "%mc_file%.tmp" "%mc_file%" >nul
    echo VSync disabled for Minecraft.
)

if exist "%mc_preview_file%" (
    echo.
    echo Disabling VSync for Minecraft Preview...

    attrib -r "%mc_preview_file%" >nul 2>&1
    
    (for /f "tokens=1,* delims=:" %%A in ('type "%mc_preview_file%"') do (
        if /i "%%A"=="gfx_vsync" (
            echo gfx_vsync:0
        ) else (
            echo %%A:%%B
        )
    )) > "%mc_preview_file%.tmp"
    move /y "%mc_preview_file%.tmp" "%mc_preview_file%" >nul
    echo VSync disabled for Minecraft Preview.
)

echo.
echo VSync settings updated. Returning to menu...
exit /b