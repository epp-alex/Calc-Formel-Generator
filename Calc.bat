@echo off
cd /d "%~dp0"

:: Wir setzen den Pfad und starten python.exe unsichtbar im Hintergrund (/b)
set "PATH=%~dp0python;%SystemRoot%\System32;%SystemRoot%;%PATH%"
start /b "" "%~dp0python\pythonw.exe" "%~dp0Calc2.py"
exit
