import pytest
from pages.home_page import HomePage

from utils.faker_utils import RandomData
from utils.tools import *

fake_valid_email = RandomData.generate_fake_email()

class TestContactForm:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)

    @pytest.mark.subscription
    def test_subscription(self, test_setup):
        """Test to verify the subscription functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.check_home_page()
        self.home_page.check_subscription_header()
        self.home_page.fill_subscribe_email_field(fake_valid_email)
        self.home_page.click_subscribe_btn()
        self.home_page.check_success_subscribe_msg(HomePage.success_subscribe_msg)

        take_screenshot(self.page, "subscription")
