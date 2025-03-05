"""
Behave environment hooks.
"""
import os
from datetime import datetime
from behave.model_core import Status

from selenium.common.exceptions import WebDriverException

from utils.driver_factory import DriverFactory
from config import config


def before_all(context):
    """
    Executed once before all tests.
    """
    # Set up context attributes
    context.config_data = config
    
    # Create reports directory if it doesn't exist
    os.makedirs(config.REPORT_DIR, exist_ok=True)
    os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)
    
    # Set up Allure reporting if available
    try:
        from allure_behave.hooks import allure_report
        allure_report(context.config)
    except ImportError:
        pass


def before_feature(context, feature):
    """
    Executed before each feature.
    """
    # Log feature start
    print(f"\nFeature: {feature.name}")


def before_scenario(context, scenario):
    """
    Executed before each scenario.
    """
    # Log scenario start
    print(f"\nScenario: {scenario.name}")
    
    # Initialize WebDriver
    context.driver = DriverFactory.get_driver()
    context.driver.base_url = config.BASE_URL
    
    # Add test data to context
    from config import test_data
    context.test_data = test_data


def after_scenario(context, scenario):
    """
    Executed after each scenario.
    """
    # Take screenshot on failure
    if scenario.status == Status.failed and config.SCREENSHOT_ON_FAILURE:
        scenario_name = scenario.name.replace(' ', '_').lower()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_name = f"failed_{scenario_name}_{timestamp}"
        
        try:
            screenshot_path = os.path.join(config.SCREENSHOT_DIR, f"{screenshot_name}.png")
            context.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")
        except WebDriverException:
            print("Failed to take screenshot")
    
    # Quit WebDriver
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        context.driver = None


def after_feature(context, feature):
    """
    Executed after each feature.
    """
    # Log feature end
    print(f"\nFeature completed: {feature.name}")


def after_all(context):
    """
    Executed once after all tests.
    """
    # Clean up any remaining resources
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        context.driver = None
