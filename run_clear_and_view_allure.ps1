# PowerShell script to clear old Allure reports, run tests, and view new Allure report

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Clearing old Allure reports..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

# Remove old Allure results
if (Test-Path "reports/allure-results") {
    Remove-Item -Path "reports/allure-results" -Recurse -Force
    Write-Host "✓ Removed old allure-results directory" -ForegroundColor Green
}

if (Test-Path ".allure") {
    Remove-Item -Path ".allure" -Recurse -Force
    Write-Host "✓ Removed .allure directory" -ForegroundColor Green
}

# Remove old screenshots (optional)
# if (Test-Path "screenshots") {
#     Remove-Item -Path "screenshots" -Recurse -Force
#     Write-Host "✓ Removed screenshots directory" -ForegroundColor Green
# }

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Running tests with Allure report..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

# Run pytest with Allure
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Generating and opening Allure report..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

# Generate and serve Allure report
allure serve reports/allure-results

Write-Host ""
Write-Host "Allure report closed." -ForegroundColor Green

