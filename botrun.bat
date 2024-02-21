@echo off

call %~dp0rofl\venv\scripts\activate

cd %~dp0rofl

set TOKEN=6825153919:AAGmm7CL_s_b3YhXETpHv5lyBhNgBLu9YNk

python telegrambot.py

pause