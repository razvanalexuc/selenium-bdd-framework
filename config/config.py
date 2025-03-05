"""
Configuration settings for the test framework.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Browser configuration
BROWSER = os.getenv('BROWSER', 'chrome')  # Default browser
HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
BROWSER_WINDOW_SIZE = os.getenv('BROWSER_WINDOW_SIZE', '1920,1080')
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))

# URLs
BASE_URL = os.getenv('BASE_URL', 'https://example.com')

# Test execution settings
SCREENSHOT_ON_FAILURE = os.getenv('SCREENSHOT_ON_FAILURE', 'True').lower() == 'true'
RERUN_FAILED_TESTS = os.getenv('RERUN_FAILED_TESTS', 'True').lower() == 'true'
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '2'))

# Report settings
REPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
SCREENSHOT_DIR = os.path.join(REPORT_DIR, 'screenshots')

# Ensure directories exist
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# WebDriver settings
DRIVER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'drivers')
USE_WEBDRIVER_MANAGER = os.getenv('USE_WEBDRIVER_MANAGER', 'True').lower() == 'true'
