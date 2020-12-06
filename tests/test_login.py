import pytest
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import get_logger


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.usefixtures("navigate_to_login", "get_login_credentials")
    def test_login(self, get_login_credentials):
        logger = get_logger()
        logger.info("Testing logging in!")
        login_page = LoginPage(self.driver)
        username_field = login_page.get_username_field()
        password_field = login_page.get_password_field()
        signin_button = login_page.get_signin_button()

        username_field.send_keys(get_login_credentials["USERNAME"])
        password_field.send_keys(get_login_credentials["PASSWORD"])
        signin_button.click()

        assert login_page.is_dashboard_present()
