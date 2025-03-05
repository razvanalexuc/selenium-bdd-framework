"""
WebDriver factory for creating and managing WebDriver instances.
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import config


class DriverFactory:
    """
    Factory class for creating WebDriver instances.
    """
    
    @staticmethod
    def get_driver(browser=None):
        """
        Get a WebDriver instance based on the specified browser.
        
        Args:
            browser (str, optional): Browser name. Defaults to None, which uses the browser from config.
            
        Returns:
            WebDriver: A WebDriver instance.
        """
        browser = browser or config.BROWSER
        browser = browser.lower()
        
        if browser == "chrome":
            return DriverFactory._get_chrome_driver()
        elif browser == "firefox":
            return DriverFactory._get_firefox_driver()
        elif browser == "edge":
            return DriverFactory._get_edge_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    
    @staticmethod
    def _get_chrome_driver():
        """
        Get a Chrome WebDriver instance.
        
        Returns:
            WebDriver: A Chrome WebDriver instance.
        """
        chrome_options = webdriver.ChromeOptions()
        
        if config.HEADLESS:
            chrome_options.add_argument("--headless")
            
        width, height = config.BROWSER_WINDOW_SIZE.split(',')
        chrome_options.add_argument(f"--window-size={width},{height}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        if config.USE_WEBDRIVER_MANAGER:
            service = ChromeService(ChromeDriverManager().install())
        else:
            driver_path = os.path.join(config.DRIVER_PATH, "chromedriver.exe")
            service = ChromeService(driver_path)
            
        driver = webdriver.Chrome(service=service, options=chrome_options)
        DriverFactory._configure_driver(driver)
        return driver
    
    @staticmethod
    def _get_firefox_driver():
        """
        Get a Firefox WebDriver instance.
        
        Returns:
            WebDriver: A Firefox WebDriver instance.
        """
        firefox_options = webdriver.FirefoxOptions()
        
        if config.HEADLESS:
            firefox_options.add_argument("--headless")
            
        if config.USE_WEBDRIVER_MANAGER:
            service = FirefoxService(GeckoDriverManager().install())
        else:
            driver_path = os.path.join(config.DRIVER_PATH, "geckodriver.exe")
            service = FirefoxService(driver_path)
            
        driver = webdriver.Firefox(service=service, options=firefox_options)
        DriverFactory._configure_driver(driver)
        return driver
    
    @staticmethod
    def _get_edge_driver():
        """
        Get an Edge WebDriver instance.
        
        Returns:
            WebDriver: An Edge WebDriver instance.
        """
        edge_options = webdriver.EdgeOptions()
        
        if config.HEADLESS:
            edge_options.add_argument("--headless")
            
        width, height = config.BROWSER_WINDOW_SIZE.split(',')
        edge_options.add_argument(f"--window-size={width},{height}")
        
        if config.USE_WEBDRIVER_MANAGER:
            service = EdgeService(EdgeChromiumDriverManager().install())
        else:
            driver_path = os.path.join(config.DRIVER_PATH, "msedgedriver.exe")
            service = EdgeService(driver_path)
            
        driver = webdriver.Edge(service=service, options=edge_options)
        DriverFactory._configure_driver(driver)
        return driver
    
    @staticmethod
    def _configure_driver(driver):
        """
        Configure common WebDriver settings.
        
        Args:
            driver (WebDriver): WebDriver instance to configure.
        """
        driver.implicitly_wait(config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
        
        # Set window size if not headless
        if not config.HEADLESS:
            width, height = config.BROWSER_WINDOW_SIZE.split(',')
            driver.set_window_size(int(width), int(height))
        
        return driver
