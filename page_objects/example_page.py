"""
Example page object for demonstration purposes.
"""
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.helpers import parse_test_data


class LoginPage(BasePage):
    """
    Login page object.
    """
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    
    def __init__(self, driver):
        """
        Initialize the login page object.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.url = "/login"  # Relative URL
    
    def open(self):
        """
        Open the login page.
        """
        return super().open(f"{self.driver.base_url}{self.url}")
    
    def login(self, username, password):
        """
        Login with the provided credentials.
        
        Args:
            username: Username
            password: Password
        """
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
    
    def login_as_user(self, user_type='default_user'):
        """
        Login as a specific user type.
        
        Args:
            user_type: User type from test_data
        """
        user_data = parse_test_data(user_type)
        return self.login(user_data['username'], user_data['password'])
    
    def get_error_message(self):
        """
        Get the error message text.
        
        Returns:
            str: Error message text
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """
        Check if an error message is displayed.
        
        Returns:
            bool: True if an error message is displayed, False otherwise
        """
        return self.is_element_displayed(self.ERROR_MESSAGE)


class DashboardPage(BasePage):
    """
    Dashboard page object.
    """
    # Locators
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".welcome-message")
    LOGOUT_BUTTON = (By.ID, "logout-button")
    USER_PROFILE = (By.ID, "user-profile")
    AGE_RESTRICTED_CONTENT = (By.ID, "age-restricted-content")
    
    def __init__(self, driver):
        """
        Initialize the dashboard page object.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.url = "/dashboard"  # Relative URL
    
    def open(self):
        """
        Open the dashboard page.
        """
        return super().open(f"{self.driver.base_url}{self.url}")
    
    def get_welcome_message(self):
        """
        Get the welcome message text.
        
        Returns:
            str: Welcome message text
        """
        return self.get_text(self.WELCOME_MESSAGE)
    
    def logout(self):
        """
        Click the logout button.
        """
        self.click(self.LOGOUT_BUTTON)
        return LoginPage(self.driver)
    
    def go_to_profile(self):
        """
        Click the user profile link.
        """
        self.click(self.USER_PROFILE)
        return ProfilePage(self.driver)
    
    def can_access_age_restricted_content(self):
        """
        Check if the user can access age-restricted content.
        
        Returns:
            bool: True if the user can access age-restricted content, False otherwise
        """
        return self.is_element_displayed(self.AGE_RESTRICTED_CONTENT)


class ProfilePage(BasePage):
    """
    User profile page object.
    """
    # Locators
    USERNAME_FIELD = (By.ID, "profile-username")
    EMAIL_FIELD = (By.ID, "profile-email")
    AGE_FIELD = (By.ID, "profile-age")
    SAVE_BUTTON = (By.ID, "save-profile")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")
    
    def __init__(self, driver):
        """
        Initialize the profile page object.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.url = "/profile"  # Relative URL
    
    def open(self):
        """
        Open the profile page.
        """
        return super().open(f"{self.driver.base_url}{self.url}")
    
    def get_username(self):
        """
        Get the username from the profile.
        
        Returns:
            str: Username
        """
        return self.get_attribute(self.USERNAME_FIELD, "value")
    
    def get_email(self):
        """
        Get the email from the profile.
        
        Returns:
            str: Email
        """
        return self.get_attribute(self.EMAIL_FIELD, "value")
    
    def get_age(self):
        """
        Get the age from the profile.
        
        Returns:
            str: Age
        """
        return self.get_attribute(self.AGE_FIELD, "value")
    
    def update_profile(self, username=None, email=None, age=None):
        """
        Update the profile with the provided information.
        
        Args:
            username: Optional new username
            email: Optional new email
            age: Optional new age
        """
        if username:
            self.input_text(self.USERNAME_FIELD, username)
        if email:
            self.input_text(self.EMAIL_FIELD, email)
        if age:
            self.input_text(self.AGE_FIELD, str(age))
        
        self.click(self.SAVE_BUTTON)
        return self
    
    def is_success_message_displayed(self):
        """
        Check if a success message is displayed.
        
        Returns:
            bool: True if a success message is displayed, False otherwise
        """
        return self.is_element_displayed(self.SUCCESS_MESSAGE)
