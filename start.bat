@echo off
setlocal
cd /d %~dp0
echo Deleting fuseki server directory if exists...
if exist fuseki rmdir /s /Q fuseki
echo Downloading fuseki server...
curl -o fuseki.zip https://miroir.univ-lorraine.fr/apache/jena/binaries/apache-jena-fuseki-3.17.0.zip
echo Unzipping file...
tar -xf fuseki.zip
del /f /q fuseki.zip
rename apache-jena-fuseki-3.17.0 fuseki
echo Launching server...
echo F|xcopy /Y /F "shiro.ini" "fuseki\run\shiro.ini"
cd fuseki 
start fuseki-server.bat
timeout /T 15
echo Creating database: webdata-project-kb
curl "http://localhost:3030/$/datasets" -H "Authorization: Basic $(echo -n admin:password | base64)" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" --data "dbName=webdata-project-kb&dbType=tdb"
echo Filling database with existing JSON-LD files...
cd ..
cd server
cd fuseki_managements
python populate-db.py
pause