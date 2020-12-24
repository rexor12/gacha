@echo off

echo Building the package...
set curdir=%cd%
cd /D "%~dp0"
python setup.py sdist bdist_wheel
REM TODO Check if the /D switch is needed to restore the current directory when the drive letter is different.
cd %curdir%
echo Build complete.