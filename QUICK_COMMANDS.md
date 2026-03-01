# Quick Commands Reference

## Run Tests and View Allure Report (Clear Old Reports)

### Option 1: Batch File (Recommended for Windows)
```bash
run_clear_and_view_allure.bat
```
**Double-click the file or run:**
```cmd
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
run_clear_and_view_allure.bat
```

### Option 2: PowerShell Script
```powershell
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
.\run_clear_and_view_allure.ps1
```

### Option 3: Manual Command (Command Prompt)
```bash
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
rmdir /s /q reports\allure-results
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Option 4: Manual Command (PowerShell)
```powershell
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
Remove-Item -Path "reports/allure-results" -Recurse -Force -ErrorAction SilentlyContinue
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## Other Useful Commands

### Run Tests Only (Without Clearing)
```bash
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results
```

### Run Tests with Both HTML and Allure Reports
```bash
python -m pytest Tests/test_login.py -v --html=reports/report.html --self-contained-html --alluredir=reports/allure-results
```

### Run Only Valid Login Tests
```bash
python -m pytest Tests/test_login.py -v -m valid_login --alluredir=reports/allure-results
```

### Run Only Invalid Login Tests
```bash
python -m pytest Tests/test_login.py -v -m invalid_login --alluredir=reports/allure-results
```

### Run Tests with Verbose Output (Show Prints)
```bash
python -m pytest Tests/test_login.py -v -s --alluredir=reports/allure-results
```

### View Existing Allure Report (Without Running Tests)
```bash
allure serve reports/allure-results
```

### View HTML Report
```bash
start reports/report.html
```

---

## What Happens When You Run

1. **Clear Phase:**
   - Removes `reports/allure-results/` directory
   - Removes `.allure/` temporary directory
   - Cleans up old report data

2. **Test Phase:**
   - Runs all 4 tests (3 valid login + 1 invalid login)
   - Captures screenshots on any failures
   - Generates Allure report JSON files

3. **View Phase:**
   - Starts Allure server
   - Opens Allure report in your default browser
   - Shows interactive dashboard with test results, steps, and screenshots

---

## Report Contents

### Allure Dashboard Shows:
- ✓ Test results (passed/failed)
- ✓ Test names and status
- ✓ Test duration/timing
- ✓ Feature categorization
- ✓ Test steps with descriptions
- ✓ Screenshots (if tests fail)
- ✓ Error messages (text attachments)
- ✓ Test timeline

### Features Visible:
- **Feature:** Login
- **Stories:** 
  - Valid User Login (3 tests)
  - Invalid User Login (1 test)
- **Severity:** CRITICAL

---

## Troubleshooting

### Allure command not found
Install Allure CLI:
```bash
npm install -g allure-commandline
```

### Port already in use error
- Allure will automatically use a different port
- Check the console output for the actual URL (e.g., http://localhost:4040)

### No screenshots in Allure report
- Ensure tests are actually failing
- Check `screenshots/` directory for files
- Run test again to generate new screenshots

### Permission denied error
- Run Command Prompt/PowerShell as Administrator
- Or modify script permissions

---

## Script Details

### run_clear_and_view_allure.bat
- **Type:** Batch file
- **OS:** Windows
- **Usage:** Double-click or run from command line
- **What it does:**
  1. Deletes old allure-results
  2. Runs pytest with Allure plugin
  3. Serves Allure report

### run_clear_and_view_allure.ps1
- **Type:** PowerShell script
- **OS:** Windows (PowerShell 5.0+)
- **Usage:** Right-click → Run with PowerShell
- **What it does:**
  1. Shows colored output
  2. Deletes old allure-results
  3. Runs pytest with Allure plugin
  4. Serves Allure report

---

## File Locations

- **Test Files:** `Tests/test_login.py`
- **Allure Results:** `reports/allure-results/`
- **Screenshots:** `screenshots/`
- **Allure Temp:** `.allure/` (auto-created)
- **Run Scripts:** `run_clear_and_view_allure.bat`, `run_clear_and_view_allure.ps1`

---

**✅ Setup Complete! You're ready to run tests with Allure reports!**

