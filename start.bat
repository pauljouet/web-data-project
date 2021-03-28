@echo off
setlocal
cd /d %~dp0
echo Launching fuseki server...
cd fuseki 
start fuseki-server.bat
timeout /T 10
cd ..
cd server
echo Launching flask server...
start start-flask.bat
timeout /T 10
cd ..
cd client
echo Launching webapp...
npm start
pause