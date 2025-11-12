\
        @echo off
        REM Example install script - register service using nssm or pywin32
        echo Installing AIDES-Windows service...
        REM You can use nssm to wrap python script as service:
        REM nssm install AIDES-Windows "C:\Python39\python.exe" "%~dp0\..\aides\main.py"
        echo Done.
