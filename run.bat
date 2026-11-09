@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  py run_local.py
  exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
  python run_local.py
  exit /b %errorlevel%
)

echo Python 3 was not found. Install Python and run this file again.
echo https://www.python.org/downloads/windows/
pause
exit /b 1
