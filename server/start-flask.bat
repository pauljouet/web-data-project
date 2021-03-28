@echo off
setlocal
cd /d %~dp0
cd ..
call env\Scripts\activate.bat
cd server
python app.py