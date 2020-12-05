import inspect
import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self, log_level=logging.DEBUG):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(log_level)
        return logger

    def verify_element_presence(self, element):
        return WebDriverWait(self.driver, 10).until(element)

    def select_option_by_text(self, element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
