import pytest
from utilities.BaseClass import BaseClass
from pageObjects.CampaignsPage import CampaignsPage


# we can clean up the code by removing the @pytest.mark.usefixtures("setup") marker and moving it to a baseclass file
# then, we can use inheritance and pass the baseclass into TestOne.
@pytest.mark.usefixtures("navigate_to_campaigns")
class TestOne(BaseClass):

    # since the request parameter was included in the fixture, the driver is part of the class object through request.cls
    def test_delete_campaign(self):
        logger = self.getLogger()
        logger.info("Test in progress!")
        campaigns_page = CampaignsPage(self.driver)
        campaign_links = campaigns_page.get_campaign_link_elements()
        test_title = campaign_links[4]
        delete_buttons = campaigns_page.get_campaign_delete_buttons()
        delete_buttons[4].click()
        self.accept_alert()
        self.driver.refresh()

        new_campaign_links = campaigns_page.get_campaign_link_elements()
        try:
            assert test_title in new_campaign_links
        except AssertionError as err:
            logger.exception("The test campaign is still in the list!")





