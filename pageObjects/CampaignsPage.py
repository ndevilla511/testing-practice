from selenium.webdriver.common.by import By


class CampaignsPage:
    # locators
    campaign_link = (By.XPATH, "//h4[@class='MuiTypography-root MuiTypography-h4']/parent::a")
    delete_buttons = (By.XPATH, "//button[contains(., 'Delete')]")
    settings_tab = (By.XPATH, "//span[text()='Settings']/parent::button")
    campaign_description = (By.ID, "description")
    settings_save = (By.XPATH, "//span[text()='Save']/parent::button")
    create_campaign = (By.XPATH, "//span[text()='Create Campaign']/parent::button")

    def __init__(self, driver):
        self.driver = driver

    def get_create_campaign_button(self):
        return self.driver.find_element(*CampaignsPage.create_campaign)

    def get_campaign_link_elements(self):
        return self.driver.find_elements(*CampaignsPage.campaign_link)

    def get_campaign_delete_buttons(self):
        return self.driver.find_elements(*CampaignsPage.delete_buttons)

    def get_settings_tab(self):
        return self.driver.find_element(*CampaignsPage.settings_tab)

    def get_description_field(self):
        return self.driver.find_element(*CampaignsPage.campaign_description)

    def get_settings_save_button(self):
        return self.driver.find_element(*CampaignsPage.settings_save)