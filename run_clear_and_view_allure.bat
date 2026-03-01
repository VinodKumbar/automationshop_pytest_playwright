@echo off
REM Script to clear old Allure reports, run tests, and view new Allure report

echo ========================================
echo Clearing old Allure reports...
echo ========================================
if exist reports\allure-results rmdir /s /q reports\allure-results
if exist .allure rmdir /s /q .allure
echo Old Allure reports cleared!

echo.
echo ========================================
echo Running tests with Allure report...
echo ========================================
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results

echo.
echo ========================================
echo Generating and opening Allure report...
echo ========================================
allure serve reports/allure-results

pause

