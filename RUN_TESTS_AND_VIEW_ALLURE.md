# ✅ Allure Report Setup - COMPLETE

## 🎯 MAIN COMMANDS TO RUN TESTS & VIEW ALLURE REPORT

### **EASIEST: Double-Click This File**
```
run_clear_and_view_allure.bat
```
✓ Clears old Allure reports
✓ Runs all tests
✓ Opens Allure report in browser

---

### **COMMAND LINE: Run This Command**

**Command Prompt (cmd.exe):**
```cmd
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
run_clear_and_view_allure.bat
```

**PowerShell:**
```powershell
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
.\run_clear_and_view_allure.ps1
```

---

## 📋 WHAT EACH SCRIPT DOES

### `run_clear_and_view_allure.bat` (RECOMMENDED)
1. ✓ Deletes old `reports/allure-results/` directory
2. ✓ Runs: `pytest Tests/test_login.py -v --alluredir=reports/allure-results`
3. ✓ Runs: `allure serve reports/allure-results`
4. ✓ Opens Allure report in your browser automatically

**Best for:** Most users, simple one-click solution

---

### `run_clear_and_view_allure.ps1` (ADVANCED)
Same as .bat but with:
- ✓ Colored console output
- ✓ Better status messages
- ✓ PowerShell-specific features

**Best for:** PowerShell users who want pretty output

---

### Other Available Scripts

| File | Purpose | Use When |
|------|---------|----------|
| `run_tests_with_allure.bat` | Run tests without clearing old reports | You want to keep history |
| `view_allure_report.bat` | View existing Allure report | Reports already generated |
| `run_clear_and_view_allure.bat` | **MAIN SCRIPT** | You want fresh reports |

---

## 📊 WHAT GETS GENERATED

After running the script, you'll get:

### 1. **Allure Report** (Interactive Dashboard)
- Location: `reports/allure-results/`
- Contains: Test results, screenshots, error messages, timeline
- Opens automatically in browser
- Shows:
  - 4 tests total (3 valid login, 1 invalid login)
  - Test status (PASSED/FAILED)
  - Test steps with descriptions
  - Screenshots on failures
  - Error messages as text attachments
  - Timing/duration for each test

### 2. **Screenshots**
- Location: `screenshots/`
- Contains: `error_message_*.png` for invalid login tests
- Contains: `failure_*.png` for any test failures

### 3. **Test Reports**
- Allure JSON files in `reports/allure-results/`
- HTML report in `reports/report.html` (if you run with --html flag)

---

## 🔍 ALLURE REPORT FEATURES

When you open the Allure report, you'll see:

### Dashboard Tab
```
┌─ Overview ──────────────────────────────────────┐
│ Total Tests: 4                                   │
│ Passed: 3-4                                      │
│ Failed: 0-1                                      │
│ Skipped: 0                                       │
│ Duration: ~67 seconds                            │
└─────────────────────────────────────────────────┘
```

### Tests Tab
- List of all test cases
- Click test to see details
- View test steps
- See attached screenshots
- Read error messages

### Suites Tab
- Grouped by feature (Login)
- Grouped by story (Valid/Invalid Login)
- Shows test results by category

### Timeline Tab
- Visual timeline of test execution
- Shows test order and duration
- Step-by-step breakdown

### Graphs Tab
- Test status pie chart
- Duration distribution
- Trends over time

---

## 💻 QUICK REFERENCE

### To Clear Reports & Run Tests with Allure
```bash
run_clear_and_view_allure.bat
```

### To Run Tests Without Clearing
```bash
python -m pytest Tests/test_login.py -v --alluredir=reports/allure-results
```

### To View Existing Allure Report
```bash
allure serve reports/allure-results
```

### To Run Only Valid Login Tests
```bash
python -m pytest Tests/test_login.py -v -m valid_login --alluredir=reports/allure-results
```

### To Run Only Invalid Login Tests
```bash
python -m pytest Tests/test_login.py -v -m invalid_login --alluredir=reports/allure-results
```

### To View HTML Report
```bash
start reports/report.html
```

---

## 🛠️ TROUBLESHOOTING

### "Allure command not found" or "allure: The term 'allure' is not recognized"
**Solution:** Install Allure CLI
```bash
npm install -g allure-commandline
```

### Port 4040 already in use
**Solution:** Allure automatically finds next available port. Check console output for actual URL.

### No screenshots in Allure report
**Possible causes:**
- Tests didn't actually fail (screenshots only on failure)
- Check `screenshots/` folder manually
- Run tests again to generate new screenshots

### Script won't run from PowerShell
**Solution:** Enable script execution
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Permission denied
**Solution:** Run as Administrator
- Right-click Command Prompt → "Run as administrator"
- Right-click PowerShell → "Run as administrator"

---

## 📁 PROJECT STRUCTURE

```
vinod_automationshop_pytest_playwright/
├── Tests/
│   ├── test_login.py                    (Main tests)
│   └── test_failure_demo.py             (Demo test - optional)
├── Pages/
│   └── login_page.py                    (Page Object Model)
├── TestData/
│   └── login_data.json                  (Test data)
├── reports/
│   ├── report.html                      (HTML report - optional)
│   └── allure-results/                  (Allure report data)
├── screenshots/
│   ├── error_message_wrong.png
│   └── failure_*.png                    (On test failure)
│
├── conftest.py                          (Pytest config & fixtures)
├── pytest.ini                           (Pytest settings)
├── requirements.txt                     (Dependencies)
│
├── run_clear_and_view_allure.bat        ⭐ MAIN SCRIPT
├── run_clear_and_view_allure.ps1        (PowerShell version)
├── run_tests_with_allure.bat            (Without clearing)
├── view_allure_report.bat               (View existing report)
│
├── README.md                            (Full documentation)
├── QUICK_COMMANDS.md                    (Command reference)
├── ALLURE_SETUP.md                      (Setup details)
└── this file                            (You are here!)
```

---

## ✨ WHAT'S CONFIGURED

✅ **Pytest** with Playwright
✅ **Allure Reports** with step tracking
✅ **Automatic Screenshots** on test failure
✅ **Screenshot Attachments** to Allure report
✅ **Error Message Logging** to Allure report
✅ **HTML Reports** for backup viewing
✅ **Parameterized Tests** (3 valid users + 1 invalid)
✅ **Page Object Model** pattern
✅ **Test Markers** for organization
✅ **Auto-execute Scripts** for easy testing

---

## 🚀 NEXT STEPS

### 1. **Run Tests**
Double-click: `run_clear_and_view_allure.bat`

### 2. **View Report**
Browser will open automatically with Allure dashboard

### 3. **Analyze Results**
- Check test status
- View test steps
- Look at screenshots
- Read error messages

### 4. **Make Changes**
- Edit tests in `Tests/test_login.py`
- Update test data in `TestData/login_data.json`
- Run again to see new results

---

## 📞 SUPPORT

For detailed information, see:
- `README.md` - Full documentation
- `ALLURE_SETUP.md` - Setup details
- `QUICK_COMMANDS.md` - All available commands

---

**🎉 Everything is ready to use!**

**Just double-click: `run_clear_and_view_allure.bat`**

