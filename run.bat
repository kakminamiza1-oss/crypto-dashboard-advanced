@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  start "Momentum Desk server" cmd /k py -m http.server 8080 --bind 127.0.0.1
) else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Python was not found. Install Python 3, then run this file again.
    echo https://www.python.org/downloads/windows/
    pause
    exit /b 1
  )
  start "Momentum Desk server" cmd /k python -m http.server 8080 --bind 127.0.0.1
)

timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8080/
