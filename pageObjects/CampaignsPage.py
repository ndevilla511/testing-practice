from selenium.webdriver.common.by import By
from utilities.selenium_utilities import SeleniumDriver
from utilities.custom_logger import get_logger


class CampaignsPage(SeleniumDriver):
    logger = get_logger()
    # locator_tuples
    _campaign_links = (By.XPATH, "//h4[@class='MuiTypography-root MuiTypography-h4']/parent::a")
    _delete_buttons = (By.XPATH, "//button[contains(., 'Delete')]")
    _settings_tab = (By.XPATH, "//span[text()='Settings']/parent::button")
    _campaign_description = (By.ID, "description")
    _settings_save = (By.XPATH, "//span[text()='Save']/parent::button")
    _create_campaign = (By.XPATH, "//span[text()='Create Campaign']/parent::button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_create_campaign_button(self):
        return self.get_element(CampaignsPage._create_campaign)

    def get_campaign_link_elements(self):
        return self.get_elements(CampaignsPage._campaign_links)

    def get_campaign_delete_buttons(self):
        return self.get_elements(CampaignsPage._delete_buttons)

    def get_settings_tab(self):
        return self.driver.get_element(CampaignsPage._settings_tab)

    def get_description_field(self):
        return self.driver.get_element(CampaignsPage._campaign_description)

    def get_settings_save_button(self):
        return self.driver.get_element(CampaignsPage._settings_save)
