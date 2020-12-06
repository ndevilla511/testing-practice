import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def select_option_by_text(self, element, text):
        select = Select(element)
        select.select_by_visible_text(text)


