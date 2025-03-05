@echo off
echo Setting up Selenium BDD Framework environment...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python 3.8 or higher.
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo Setup complete! Virtual environment is activated.
echo To run tests, use:
echo     behave features/
echo     or
echo     pytest
echo.
echo To deactivate the virtual environment when done, type:
echo     deactivate
echo.
