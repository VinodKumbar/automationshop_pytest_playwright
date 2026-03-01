import json
import pytest
from playwright.sync_api import expect

from Pages.login_page import LoginPage

try:
    import allure
    ALLURE_AVAILABLE = True
except ImportError:
    ALLURE_AVAILABLE = False


def load_test_data():
    with open("TestData/login_data.json") as f:
        return json.load(f)


# Get test data for parameterization
test_data = load_test_data()
valid_users = test_data["valid_users"]
invalid_users = test_data["invalid_users"]


@pytest.mark.valid_login
@pytest.mark.parametrize("user", valid_users)
def test_valid_login(page, user):
    """Test valid user login and logout"""
    if ALLURE_AVAILABLE:
        allure.dynamic.feature("Login")
        allure.dynamic.story("Valid User Login")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

    login_page = LoginPage(page)

    # Step 1: Navigate to login page
    if ALLURE_AVAILABLE:
        with allure.step(f"Navigate to application"):
            login_page.navigate()
    else:
        login_page.navigate()

    # Step 2: Login with valid credentials
    if ALLURE_AVAILABLE:
        with allure.step(f"Login with username: {user['username']}"):
            login_page.login(user["username"], user["password"])
    else:
        login_page.login(user["username"], user["password"])

    # Step 3: Verify user is logged in
    if ALLURE_AVAILABLE:
        with allure.step("Verify user is redirected to products page"):
            assert "products" in page.url, "User should be redirected to products page"
    else:
        assert "products" in page.url, "User should be redirected to products page"

    # Step 4: Logout
    if ALLURE_AVAILABLE:
        with allure.step("Logout from application"):
            login_page.logout()
    else:
        login_page.logout()


@pytest.mark.invalid_login
@pytest.mark.parametrize("user", invalid_users)
def test_invalid_login(page, user):
    """Test invalid user login with error message validation"""
    if ALLURE_AVAILABLE:
        allure.dynamic.feature("Login")
        allure.dynamic.story("Invalid User Login")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

    login_page = LoginPage(page)

    # Step 1: Navigate to login page
    if ALLURE_AVAILABLE:
        with allure.step("Navigate to application"):
            login_page.navigate()
    else:
        login_page.navigate()

    # Step 2: Attempt login with invalid credentials
    if ALLURE_AVAILABLE:
        with allure.step(f"Attempt login with invalid credentials - username: {user['username']}"):
            login_page.login(user["username"], user["password"])
    else:
        login_page.login(user["username"], user["password"])

    # Step 3: Wait for error message
    if ALLURE_AVAILABLE:
        with allure.step("Wait for error message to appear"):
            page.wait_for_timeout(2000)
    else:
        page.wait_for_timeout(2000)

    # Step 4: Verify error message
    if ALLURE_AVAILABLE:
        with allure.step("Verify error message is displayed"):
            error_locator = page.locator("#errorModal > div > p")
            if error_locator.count() > 0:
                error_message = error_locator.inner_text()
                print(f"Error message: {error_message}")
                allure.attach(error_message, name="Error Message", attachment_type=allure.attachment_type.TEXT)

            expect(error_locator).to_be_visible()
            expect(error_locator).to_contain_text("Invalid")
    else:
        error_locator = page.locator("#errorModal > div > p")
        if error_locator.count() > 0:
            error_message = error_locator.inner_text()
            print(f"Error message: {error_message}")

        expect(error_locator).to_be_visible()
        expect(error_locator).to_contain_text("Invalid")

    # Step 5: Capture screenshot
    if ALLURE_AVAILABLE:
        with allure.step("Capture screenshot of error"):
            page.screenshot(path=f"screenshots/error_message_{user['username']}.png")
            allure.attach.file(
                f"screenshots/error_message_{user['username']}.png",
                name="Error Message Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    else:
        page.screenshot(path=f"screenshots/error_message_{user['username']}.png")


