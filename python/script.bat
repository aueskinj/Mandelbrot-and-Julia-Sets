:: filepath: /c:/Users/Administrator/Desktop/projects/Sets/Mandelbrot-and-Julia-Sets/python/scriptswin.bat
@echo off

:: Step 1: Create virtual environment
py -m venv venv

:: Step 2: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 3: Upgrade pip
echo Upgrading pip...
pip install --upgrade pip

:: Step 4: Install requirements
echo Installing requirements from requirements.txt...
pip install -r requirements.txt

:: Step 5: Confirmation
echo Setup complete. Virtual environment 'venv' is ready and dependencies are installed.
echo To activate the virtual environment, run: venv\Scripts\activate