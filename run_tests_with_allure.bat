@echo off
REM Install required packages
echo Installing dependencies...
python -m pip install allure-pytest allure-python-commons -q

REM Run tests with Allure report
echo Running tests with Allure report generation...
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results

echo.
echo Test execution completed!
echo.
echo To view Allure report, run:
echo   allure serve reports/allure-results

