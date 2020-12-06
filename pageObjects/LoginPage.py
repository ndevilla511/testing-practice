from selenium.webdriver.common.by import By
from utilities.selenium_utilities import SeleniumDriver
from utilities.custom_logger import get_logger


class LoginPage(SeleniumDriver):
    logger = get_logger()
    # locator_tuples
    _username = (By.NAME, "username")
    _password = (By.NAME, "password")
    _signin_button = (By.XPATH, "//button[@type='submit' and contains(., 'Sign In')]")
    _dashboard = (By.XPATH, "//h1[contains(.,'Dashboard')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_username_field(self):
        return self.get_element(LoginPage._username)

    def get_password_field(self):
        return self.get_element(LoginPage._password)

    def get_signin_button(self):
        return self.get_element(LoginPage._signin_button)

    def is_dashboard_present(self):
        return self.is_element_present(LoginPage._dashboard)
    
    def login(self, username, password):
        username_field = self.get_username_field()
        password_field = self.get_password_field()
        signin_button = self.get_signin_button()

        username_field.send_keys(username)
        password_field.send_keys(password)
        signin_button.click()

        self.wait_for_element(LoginPage._dashboard)
