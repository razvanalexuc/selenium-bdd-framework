"""
Helper functions for the test framework.
"""
import os
import time
import random
import string
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config import config


def take_screenshot(driver, name=None):
    """
    Take a screenshot and save it to the screenshots directory.
    
    Args:
        driver: WebDriver instance
        name: Optional name for the screenshot
        
    Returns:
        str: Path to the saved screenshot
    """
    if name is None:
        name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Ensure filename is valid
    name = ''.join(c for c in name if c.isalnum() or c in ['_', '-', '.'])
    
    # Add timestamp to prevent overwriting
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{name}_{timestamp}.png"
    
    screenshot_path = os.path.join(config.SCREENSHOT_DIR, filename)
    driver.save_screenshot(screenshot_path)
    
    return screenshot_path


def wait_for_element(driver, locator, timeout=None):
    """
    Wait for an element to be present and visible.
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Optional timeout in seconds
        
    Returns:
        WebElement: The found element
        
    Raises:
        TimeoutException: If the element is not found within the timeout
    """
    timeout = timeout or config.IMPLICIT_WAIT
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))


def wait_for_element_clickable(driver, locator, timeout=None):
    """
    Wait for an element to be clickable.
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Optional timeout in seconds
        
    Returns:
        WebElement: The found element
        
    Raises:
        TimeoutException: If the element is not clickable within the timeout
    """
    timeout = timeout or config.IMPLICIT_WAIT
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))


def is_element_present(driver, locator, timeout=5):
    """
    Check if an element is present on the page.
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Optional timeout in seconds
        
    Returns:
        bool: True if the element is present, False otherwise
    """
    try:
        wait_for_element(driver, locator, timeout)
        return True
    except (TimeoutException, NoSuchElementException):
        return False


def generate_random_string(length=10):
    """
    Generate a random string of fixed length.
    
    Args:
        length: Length of the string
        
    Returns:
        str: Random string
    """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def parse_test_data(data_key, data_dict=None):
    """
    Parse test data from the test_data module or a provided dictionary.
    
    Args:
        data_key: Key to look up in the data dictionary
        data_dict: Optional dictionary to look up the key in
        
    Returns:
        The value associated with the key
    """
    if data_dict is None:
        from config import test_data
        # Try to get the data from different dictionaries in test_data
        for dict_name in ['USER_DATA', 'PRODUCT_DATA', 'FORM_DATA', 'SCENARIOS', 'ENVIRONMENTS']:
            data_dict = getattr(test_data, dict_name, {})
            if data_key in data_dict:
                return data_dict[data_key]
        
        # If not found in any dictionary, try to call a getter function
        for func_name in ['get_user_data', 'get_scenario_data', 'get_environment_data']:
            func = getattr(test_data, func_name, None)
            if func:
                try:
                    return func(data_key)
                except:
                    pass
        
        return None
    else:
        return data_dict.get(data_key)


def get_nested_value(data_dict, key_path):
    """
    Get a nested value from a dictionary using a dot-separated key path.
    
    Args:
        data_dict: Dictionary to get the value from
        key_path: Dot-separated key path (e.g., 'user.profile.name')
        
    Returns:
        The value at the specified key path, or None if not found
    """
    keys = key_path.split('.')
    value = data_dict
    
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    
    return value
