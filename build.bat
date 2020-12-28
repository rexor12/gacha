@echo off
setlocal
echo Building the package...
cd /D "%~dp0"
python setup.py sdist bdist_wheel
echo Build complete.