@echo off

echo Building the package...
set curdir=%cd%
cd /D "%~dp0"
python setup.py sdist bdist_wheel
cd /D %curdir%
echo Build complete.