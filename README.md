# Automation Shop Test Suite

This is a Playwright + Pytest automation test suite for the Vinod's Automation Shop application with HTML and Allure reporting capabilities.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Allure CLI (Optional, for Allure report)

**Option A: Using Chocolatey (Windows)**
```bash
choco install allure
```

**Option B: Using npm**
```bash
npm install -g allure-commandline
```

## Running Tests

### Quick Start: Run All Tests with Allure Report
```bash
cd C:\Users\VINOD\OneDrive\Desktop\vinod_automationshop_pytest_playwright
run_tests_with_allure.bat
```

### Run All Tests with Both Reports
```bash
pytest Tests/test_login.py -v --html=reports/report.html --self-contained-html --alluredir=reports/allure-results
```

### Run Only Valid Login Tests
```bash
pytest Tests/test_login.py -v -m valid_login --alluredir=reports/allure-results
```

### Run Only Invalid Login Tests
```bash
pytest Tests/test_login.py -v -m invalid_login --alluredir=reports/allure-results
```

### Run With Verbose Output
```bash
pytest Tests/test_login.py -v -s --alluredir=reports/allure-results
```

## Viewing Reports

### 1. HTML Report
- **Location:** `reports/report.html`
- **How to view:** Open `reports/report.html` in any web browser
- **Features:** 
  - Test results with pass/fail status
  - Test duration
  - Failure details
  - Self-contained (no external dependencies needed)

### 2. Allure Report
- **Location:** `reports/allure-results/`
- **How to view:** 
```bash
allure serve reports/allure-results
```
- **Features:**
  - Interactive test dashboard
  - Step-by-step test execution with screenshots
  - Failure screenshots automatically attached
  - Error messages and attachments
  - Test history and trends
  - Test categorization by feature and story
  - Timeline view

#### Quick View (Double-click):
```bash
view_allure_report.bat
```

## Report Features

### Automatic Screenshot Capture on Failure
✅ Screenshots are automatically captured when tests fail
✅ Screenshots are attached to Allure reports
✅ Error messages are captured and logged
✅ Test steps are tracked with Allure

### What Gets Captured
- Test navigation and login attempts
- Error messages and validation
- Page state at time of failure
- Test execution steps and timing

## Project Structure

```
vinod_automationshop_pytest_playwright/
├── Pages/                          # Page Object Models
│   └── login_page.py
├── TestData/                       # Test Data
│   └── login_data.json
├── Tests/                          # Test Cases
│   └── test_login.py
├── reports/                        # Generated Reports
│   ├── report.html                 # HTML Report
│   └── allure-results/             # Allure Report Data
├── screenshots/                    # Test Screenshots
│   ├── error_message_*.png
│   └── failure_*.png
├── conftest.py                     # Pytest Fixtures & Hooks
├── pytest.ini                      # Pytest Configuration
├── requirements.txt                # Python Dependencies
├── run_tests_with_allure.bat       # Run tests with Allure
├── view_allure_report.bat          # View Allure report
└── README.md                       # This File
```

## Test Details

### Login Tests (test_login.py)

#### Valid Login Test (`test_valid_login`)
- **Markers:** `@pytest.mark.valid_login`
- **Parameters:** 3 valid users (vinod, john, bruce)
- **Steps:**
  1. Navigate to login page
  2. Login with valid credentials
  3. Verify redirection to products page
  4. Logout
- **Assertions:** URL contains "products"
- **Reports:** ✓ Captured in HTML and Allure reports with step details

#### Invalid Login Test (`test_invalid_login`)
- **Markers:** `@pytest.mark.invalid_login`
- **Parameters:** 1 invalid user (wrong credentials)
- **Steps:**
  1. Navigate to login page
  2. Login with invalid credentials
  3. Wait for error message
  4. Verify error message display
  5. Capture screenshot of error
- **Assertions:** Error message visible and contains "Invalid"
- **Reports:** ✓ Captured in HTML and Allure reports with screenshot attachment

## Features

✅ Parameterized tests (test multiple users)
✅ Allure reporting with step tracking
✅ Automatic screenshot capture on failure
✅ Screenshot attachment to Allure reports
✅ HTML reporting with self-contained file
✅ Page Object Model pattern
✅ Test data externalization (JSON)
✅ Pytest markers for test organization
✅ Error message logging
✅ Test step documentation

## Configuration

### Change Browser to Headless Mode
Edit `conftest.py` and modify:
```python
browser = p.chromium.launch(headless=True)  # Set to True for headless mode
```

### Add More Test Data
Edit `TestData/login_data.json` to add more valid or invalid users

### Customize Test Markers
Edit `pytest.ini` to add more markers for test organization

## Troubleshooting

### Allure Report Not Showing Screenshots
- Ensure `allure-pytest` is installed: `pip install allure-pytest`
- Check `reports/allure-results/` directory exists
- Run: `allure serve reports/allure-results`

### Port Already in Use (for Allure serve)
- Allure will automatically select a different port
- Check console output for the URL

### Screenshots Not Captured
- Verify `screenshots/` directory exists
- Check test output for screenshot save confirmation

## Dependencies

- **pytest** - Test framework
- **playwright** - Browser automation
- **pytest-html** - HTML reporting
- **allure-pytest** - Allure reporting
- **allure-python-commons** - Allure integration
- **pytest-base-url** - Base URL fixture
- **pytest-playwright** - Playwright integration

