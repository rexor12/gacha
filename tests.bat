@echo off
setlocal
echo Running unit tests..
cd /D "%~dp0"
python -m unittest -v
echo Running unit tests complete.