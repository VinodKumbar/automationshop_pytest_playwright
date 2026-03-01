import pytest
import os
from playwright.sync_api import sync_playwright
from utils.reporting import attach_screenshot, AllureHelper


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshot on test failure and attach to Allure report
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Try to get screenshot from the test
        if hasattr(item, "funcargs") and "page" in item.funcargs:
            page = item.funcargs["page"]

            # Create screenshots directory if it doesn't exist
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/failure_{item.name}.png"
            try:
                page.screenshot(path=screenshot_path)
                print(f"\n✓ Screenshot saved: {screenshot_path}")

                # Attach to Allure report using helper
                attach_screenshot(screenshot_path, f"Failure Screenshot - {item.name}")
                print(f"✓ Screenshot attached to Allure report")

            except Exception as e:
                print(f"✗ Failed to capture screenshot: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    """
    Add test name and description to Allure report
    """
    if AllureHelper.is_available():
        # Add test description using helper
        try:
            from utils.reporting import allure
            if allure:
                allure.dynamic.title(item.name)
                allure.dynamic.description(f"Test: {item.name}")
        except:
            pass

    yield
