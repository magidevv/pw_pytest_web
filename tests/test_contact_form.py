import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactUsPage

from utils.faker_utils import RandomData
from utils.tools import *

fake_valid_name = RandomData.generate_fake_name()
fake_valid_email = RandomData.generate_fake_email()
fake_valid_subject = RandomData.generate_fake_subject()
fake_valid_message = RandomData.generate_fake_message()

class TestContactForm:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.contact_us_page = ContactUsPage(self.page)

    @pytest.mark.contact_form
    def test_contact_form(self, test_setup):
        """Test to verify the contact us form functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.check_home_page()
        self.home_page.click_contact_us_btn()
        self.contact_us_page.check_contact_us_header()
        self.contact_us_page.fill_contact_us_form(fake_valid_name, fake_valid_email, fake_valid_subject, fake_valid_message)
        self.contact_us_page.upload_file()
        self.contact_us_page.click_ok_btn()
        self.contact_us_page.check_alert_success()
        self.contact_us_page.click_home_btn()
        self.home_page.check_home_page()

        take_screenshot(self.page, "contact_form")
