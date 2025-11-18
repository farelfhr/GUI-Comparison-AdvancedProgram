@echo off
setlocal
set PYTHON_BIN=python
pushd %~dp0

start "Tkinter Hello" cmd /k "%PYTHON_BIN% src\01_tkinter_hello.py"
start "Kivy Hello" cmd /k "%PYTHON_BIN% src\02_kivy_hello.py"
start "DearPyGui Hello" cmd /k "%PYTHON_BIN% src\03_dearpygui_hello.py"
start "Remi Hello" cmd /k "%PYTHON_BIN% src\04_remi_hello.py"

popd
endlocal
exit /b 0

