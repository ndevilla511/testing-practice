import pytest
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.custom_logger import get_logger


class SeleniumDriver:
    logger = get_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_tuple):
        (by_type, locator) = locator_tuple
        element = None
        try:
            element = self.driver.find_element(by_type, locator)
            self.logger.info("Element Found")
        except:
            self.logger.info("Element not found")
        return element

    def get_elements(self, locator_tuple):
        (by_type, locator) = locator_tuple
        element = None
        try:
            element = self.driver.find_elements(by_type, locator)
            self.logger.info("Elements found")
        except:
            self.logger.info("Elements not found")
        return element

    def click_element(self, locator_tuple):
        (by_type, locator) = locator_tuple
        try:
            element = self.get_element(locator_tuple)
            element.click()
            self.logger.info("Clicked on element with locator: " + locator + " locatorType: " + str(by_type))
        except:
            self.logger.info("Cannot click on the element with locator: " + locator + " locatorType: " + str(by_type))
            print_stack()

    def is_element_present(self, locator_tuple):
        (by_type, locator) = locator_tuple
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                self.logger.info("Element Found")
                return True
            else:
                self.logger.info("Element not found")
                return False
        except:
            self.logger.info("Element not found")
            return False

    def are_elements_present(self, locator_tuple):
        (by_type, locator) = locator_tuple
        try:
            elements_list = self.driver.find_elements(by_type, locator)
            if len(elements_list) > 0:
                self.logger.info("Element(s) Found")
                return True
            else:
                self.logger.info("Element(s) not found")
                return False
        except:
            self.logger.info("Element(s) not found")
            return False

    def wait_for_element(self, locator_tuple,
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            self.logger.info("Waiting for maximum :: " + str(timeout) +
                             " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.presence_of_element_located(locator_tuple))
            self.logger.info("Element appeared on the web page")
        except:
            self.logger.info("Element not appeared on the web page")
            print_stack()
        return element

    def accept_alert(self):
        self.driver.switch_to.alert.accept()