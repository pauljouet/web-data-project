@echo off
setlocal
cd /d %~dp0
if not exist env python -m venv env
env\Scripts\activate.bat
pip install -r server\requirements.txt
