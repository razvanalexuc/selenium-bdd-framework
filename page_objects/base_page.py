"""
Base page object class that all page objects will inherit from.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from config import config
from utils.helpers import take_screenshot


class BasePage:
    """
    Base page object class with common methods for all pages.
    """
    
    def __init__(self, driver):
        """
        Initialize the base page object.
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.IMPLICIT_WAIT)
    
    def open(self, url=None):
        """
        Open a URL in the browser.
        
        Args:
            url: URL to open, defaults to BASE_URL from config
        """
        url = url or config.BASE_URL
        self.driver.get(url)
        return self
    
    def find_element(self, locator):
        """
        Find an element on the page.
        
        Args:
            locator: Tuple of (By, selector)
            
        Returns:
            WebElement: The found element
        """
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """
        Find multiple elements on the page.
        
        Args:
            locator: Tuple of (By, selector)
            
        Returns:
            list: List of WebElements
        """
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        """
        Click on an element.
        
        Args:
            locator: Tuple of (By, selector)
        """
        element = self.wait_for_element_clickable(locator)
        element.click()
        return self
    
    def input_text(self, locator, text):
        """
        Input text into an element.
        
        Args:
            locator: Tuple of (By, selector)
            text: Text to input
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
        return self
    
    def get_text(self, locator):
        """
        Get text from an element.
        
        Args:
            locator: Tuple of (By, selector)
            
        Returns:
            str: Text of the element
        """
        element = self.wait_for_element(locator)
        return element.text
    
    def get_attribute(self, locator, attribute):
        """
        Get an attribute value from an element.
        
        Args:
            locator: Tuple of (By, selector)
            attribute: Attribute name
            
        Returns:
            str: Attribute value
        """
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute)
    
    def is_element_displayed(self, locator, timeout=5):
        """
        Check if an element is displayed.
        
        Args:
            locator: Tuple of (By, selector)
            timeout: Timeout in seconds
            
        Returns:
            bool: True if the element is displayed, False otherwise
        """
        try:
            element = self.wait_for_element(locator, timeout)
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_element(self, locator, timeout=None):
        """
        Wait for an element to be present and visible.
        
        Args:
            locator: Tuple of (By, selector)
            timeout: Optional timeout in seconds
            
        Returns:
            WebElement: The found element
        """
        timeout = timeout or config.IMPLICIT_WAIT
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Wait for an element to be clickable.
        
        Args:
            locator: Tuple of (By, selector)
            timeout: Optional timeout in seconds
            
        Returns:
            WebElement: The found element
        """
        timeout = timeout or config.IMPLICIT_WAIT
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_url_contains(self, text, timeout=None):
        """
        Wait for the URL to contain specific text.
        
        Args:
            text: Text to wait for in the URL
            timeout: Optional timeout in seconds
            
        Returns:
            bool: True if the URL contains the text, False otherwise
        """
        timeout = timeout or config.IMPLICIT_WAIT
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(text))
    
    def hover(self, locator):
        """
        Hover over an element.
        
        Args:
            locator: Tuple of (By, selector)
        """
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return self
    
    def scroll_to_element(self, locator):
        """
        Scroll to an element.
        
        Args:
            locator: Tuple of (By, selector)
        """
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self
    
    def take_screenshot(self, name=None):
        """
        Take a screenshot.
        
        Args:
            name: Optional name for the screenshot
            
        Returns:
            str: Path to the saved screenshot
        """
        return take_screenshot(self.driver, name)
    
    def get_page_title(self):
        """
        Get the page title.
        
        Returns:
            str: Page title
        """
        return self.driver.title
    
    def get_current_url(self):
        """
        Get the current URL.
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
    
    def refresh_page(self):
        """
        Refresh the current page.
        """
        self.driver.refresh()
        return self
    
    def go_back(self):
        """
        Go back to the previous page.
        """
        self.driver.back()
        return self
    
    def go_forward(self):
        """
        Go forward to the next page.
        """
        self.driver.forward()
        return self
    
    def switch_to_frame(self, locator):
        """
        Switch to an iframe.
        
        Args:
            locator: Tuple of (By, selector)
        """
        frame = self.wait_for_element(locator)
        self.driver.switch_to.frame(frame)
        return self
    
    def switch_to_default_content(self):
        """
        Switch back to the default content from an iframe.
        """
        self.driver.switch_to.default_content()
        return self
    
    def execute_script(self, script, *args):
        """
        Execute JavaScript in the current window/frame.
        
        Args:
            script: JavaScript to execute
            *args: Arguments to pass to the script
            
        Returns:
            The result of the script execution
        """
        return self.driver.execute_script(script, *args)
    
    def press_key(self, locator, key):
        """
        Press a key on an element.
        
        Args:
            locator: Tuple of (By, selector)
            key: Key to press (from selenium.webdriver.common.keys.Keys)
        """
        element = self.wait_for_element(locator)
        element.send_keys(key)
        return self
    
    def press_enter(self, locator):
        """
        Press Enter on an element.
        
        Args:
            locator: Tuple of (By, selector)
        """
        return self.press_key(locator, Keys.ENTER)
    
    def press_escape(self, locator):
        """
        Press Escape on an element.
        
        Args:
            locator: Tuple of (By, selector)
        """
        return self.press_key(locator, Keys.ESCAPE)
