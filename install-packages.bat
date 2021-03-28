@echo off
setlocal
cd /d %~dp0
if not exist env (python -m venv env)
call env\Scripts\activate.bat
echo Installing requirements...
pip install -r server\requirements.txt
cd client
npm install