@echo off
REM Script to view Allure report
REM First check if allure is installed
where allure >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Allure CLI not found. Installing allure-commandline...
    npm install -g allure-commandline
)

REM Serve the Allure report
echo Opening Allure Report...
allure serve reports/allure-results

pause

