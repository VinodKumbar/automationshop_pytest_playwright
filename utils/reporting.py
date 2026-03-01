"""
Reporting utilities for Allure and HTML reports
Provides helper functions to simplify test code
"""

import os
from contextlib import contextmanager

try:
    import allure
    ALLURE_AVAILABLE = True
except ImportError:
    allure = None
    ALLURE_AVAILABLE = False


class AllureHelper:
    """Helper class for Allure report integration"""

    @staticmethod
    def is_available():
        """Check if Allure is available"""
        return ALLURE_AVAILABLE

    @staticmethod
    def set_test_info(feature, story, severity="CRITICAL"):
        """Set test feature, story, and severity"""
        if ALLURE_AVAILABLE:
            allure.dynamic.feature(feature)
            allure.dynamic.story(story)
            if hasattr(allure.severity_level, severity):
                allure.dynamic.severity(getattr(allure.severity_level, severity))

    @staticmethod
    @contextmanager
    def step(description):
        """
        Context manager for Allure steps
        Works even when Allure is not available
        """
        if ALLURE_AVAILABLE:
            with allure.step(description):
                yield
        else:
            yield

    @staticmethod
    def attach_text(text, name="Text Attachment"):
        """Attach text to Allure report"""
        if ALLURE_AVAILABLE:
            allure.attach(
                text,
                name=name,
                attachment_type=allure.attachment_type.TEXT
            )

    @staticmethod
    def attach_screenshot(filepath, name="Screenshot"):
        """Attach screenshot file to Allure report"""
        if ALLURE_AVAILABLE and os.path.exists(filepath):
            allure.attach.file(
                filepath,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )

    @staticmethod
    def capture_and_attach_screenshot(page, filepath, name="Screenshot"):
        """
        Capture screenshot from Playwright page and attach to Allure

        Args:
            page: Playwright page object
            filepath: Path to save screenshot
            name: Name for the attachment
        """
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Capture screenshot
        page.screenshot(path=filepath)

        # Attach to Allure report
        AllureHelper.attach_screenshot(filepath, name)

        return filepath


# Create singleton instance
allure_helper = AllureHelper()


# Convenience functions
def step(description):
    """Allure step decorator/context manager"""
    return AllureHelper.step(description)


def set_test_info(feature, story, severity="CRITICAL"):
    """Set test information for Allure report"""
    AllureHelper.set_test_info(feature, story, severity)


def attach_text(text, name="Text Attachment"):
    """Attach text to report"""
    AllureHelper.attach_text(text, name)


def attach_screenshot(filepath, name="Screenshot"):
    """Attach screenshot to report"""
    AllureHelper.attach_screenshot(filepath, name)


def capture_screenshot(page, filepath, name="Screenshot"):
    """Capture and attach screenshot"""
    return AllureHelper.capture_and_attach_screenshot(page, filepath, name)

