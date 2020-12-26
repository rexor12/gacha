@echo off

echo Running unit tests..
set curdir=%cd%
cd /D "%~dp0"
echo Current directory: %cd%
python -m unittest -v
cd /D %curdir%
echo Running unit tests complete.