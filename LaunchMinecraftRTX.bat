@echo off
:START
cls
echo ================================
echo   Launch Minecraft with RTX
echo ================================
echo [1] Minecraft
echo [2] Minecraft Preview
echo.

choice /c 12 /n /m "Select an option [1/2]:"

REM Handle invalid input by restarting
if not "%errorlevel%"=="1" if not "%errorlevel%"=="2" (
    echo Invalid input. Please enter 1 or 2.
    timeout /t 2 >nul
    goto START
)

REM Set file location and protocol based on user input
if errorlevel 2 (
    set "file=%LOCALAPPDATA%\Packages\Microsoft.MinecraftWindowsBeta_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt"
    set "protocol=minecraft-preview://"
) else (
    set "file=%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt"
    set "protocol=minecraft://"
)

REM Update graphics_mode to ray tracing
(for /f "tokens=1,* delims=:" %%A in ('type "%file%"') do (
    if /i "%%A"=="graphics_mode" (
        echo graphics_mode:3
    ) else (
        echo %%A:%%B
    )
)) > "%file%.tmp"

move /y "%file%.tmp" "%file%" >nul

REM Launch Minecraft with the selected protocol
start "" "%protocol%"

exit