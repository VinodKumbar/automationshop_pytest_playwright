import json
import pytest
from playwright.sync_api import expect

from Pages.login_page import LoginPage
from utils.reporting import step, set_test_info, attach_text, capture_screenshot


def load_test_data():
    """Load test data from JSON file"""
    with open("TestData/login_data.json") as f:
        return json.load(f)


# Get test data for parameterization
test_data = load_test_data()
valid_users = test_data["valid_users"]
invalid_users = test_data["invalid_users"]


def perform_login(login_page, username, password):
    """Helper function to perform login with steps"""
    with step("Navigate to application"):
        login_page.navigate()

    with step(f"Login with username: {username}"):
        login_page.login(username, password)


def verify_error_message(page, username):
    """Helper function to verify and capture error message"""
    error_locator = page.locator("#errorModal > div > p")

    # Verify error is visible and contains expected text
    expect(error_locator).to_be_visible()
    expect(error_locator).to_contain_text("Invalid")

    # Capture error message and screenshot
    if error_locator.count() > 0:
        error_message = error_locator.inner_text()
        print(f"Error message: {error_message}")
        attach_text(error_message, "Error Message")

    capture_screenshot(page, f"screenshots/error_message_{username}.png", "Error Screenshot")


@pytest.mark.valid_login
@pytest.mark.parametrize("user", valid_users)
def test_valid_login(page, user):
    """Test valid user login and logout"""
    set_test_info("Login", "Valid User Login", "CRITICAL")

    login_page = LoginPage(page)
    perform_login(login_page, user["username"], user["password"])

    with step("Verify successful login"):
        assert "products" in page.url, "User should be redirected to products page"

    with step("Logout"):
        login_page.logout()


@pytest.mark.invalid_login
@pytest.mark.parametrize("user", invalid_users)
def test_invalid_login(page, user):
    """Test invalid user login with error message validation"""
    set_test_info("Login", "Invalid User Login", "CRITICAL")

    login_page = LoginPage(page)
    perform_login(login_page, user["username"], user["password"])

    with step("Wait for error message"):
        page.wait_for_timeout(2000)

    with step("Verify error message and capture screenshot"):
        verify_error_message(page, user["username"])



