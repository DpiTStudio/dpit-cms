@echo off
chcp 65001 > nul
cd /d "%~dp0mysite"
call ..\.venv\Scripts\activate.bat
python manage.py collectstatic --noinput
pause
