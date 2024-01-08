import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.acc_created_page import AccCreatedPage
from pages.delete_acc_page import DeleteAccPage

from utils.test_data import Data
from utils.faker_utils import RandomData
from utils.tools import *

fake_valid_name = RandomData.generate_fake_name()
stored_valid_name = fake_valid_name
fake_valid_email = RandomData.generate_fake_email()
stored_valid_email = fake_valid_email
fake_valid_password = RandomData.generate_fake_password(8)
stored_valid_password = fake_valid_password
fake_valid_first_name = RandomData.generate_fake_first_name()
fake_valid_last_name = RandomData.generate_fake_last_name()
fake_valid_company = RandomData.generate_fake_company()
fake_valid_address = RandomData.generate_fake_address()
fake_valid_state = RandomData.generate_fake_state()
fake_valid_city = RandomData.generate_fake_city()
fake_valid_zipcode = RandomData.generate_fake_postcode()
fake_valid_mobile_number = RandomData.generate_fake_phone_number()
fake_invalid_email = RandomData.generate_fake_invalid_email()
fake_invalid_password = RandomData.generate_fake_invalid_password()

class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.login_page = LoginPage(self.page)
        self.signup_page = SignupPage(self.page)
        self.acc_created_page = AccCreatedPage(self.page)
        self.delete_acc_page = DeleteAccPage(self.page)

    @pytest.mark.valid_login
    def test_valid_login(self, test_setup):
        """Test to verify the user login with valid credentials functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.click_signup_login_btn()
        self.login_page.fill_signup_form(fake_valid_name, fake_valid_email)
        self.login_page.click_signup_btn()
        self.signup_page.fill_acc_info_form(Data.title, stored_valid_name, stored_valid_email, fake_valid_password)
        self.signup_page.select_newsletter_checkbox()
        self.signup_page.select_offers_checkbox()
        self.signup_page.fill_address_info_form(fake_valid_first_name, fake_valid_last_name, fake_valid_company, fake_valid_address, fake_valid_address, Data.countries, fake_valid_state, fake_valid_city, fake_valid_zipcode, fake_valid_mobile_number)
        self.signup_page.click_create_acc_btn()
        self.acc_created_page.click_continue_btn()
        self.home_page.click_logout_btn()
        self.home_page.click_home_btn()

        self.home_page.check_home_page()
        self.home_page.click_signup_login_btn()
        self.login_page.check_login_header()
        self.login_page.fill_login_form(stored_valid_email, stored_valid_password)
        self.login_page.click_login_btn()
        self.home_page.check_loggedin_as_username_text(stored_valid_name)
        self.home_page.click_delete_acc_btn()
        self.delete_acc_page.check_acc_deleted_header()
        self.delete_acc_page.click_continue_btn()

        take_screenshot(self.page, "valid_login")

    @pytest.mark.invalid_login
    def test_invalid_login(self, test_setup):
        """Test to verify the user login with invalid credentials functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.check_home_page()
        self.home_page.click_signup_login_btn()
        self.login_page.check_login_header()
        self.login_page.fill_login_form(fake_invalid_email, fake_invalid_password)
        self.login_page.click_login_btn()
        self.login_page.check_invalid_login_error(LoginPage.login_error)

        take_screenshot(self.page, "invalid_login")

    @pytest.mark.logout
    def test_logout(self, test_setup):
        """Test to verify the user logout after successful login functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.click_signup_login_btn()
        self.login_page.fill_signup_form(fake_valid_name, fake_valid_email)
        self.login_page.click_signup_btn()
        self.signup_page.fill_acc_info_form(Data.title, stored_valid_name, stored_valid_email, fake_valid_password)
        self.signup_page.select_newsletter_checkbox()
        self.signup_page.select_offers_checkbox()
        self.signup_page.fill_address_info_form(fake_valid_first_name, fake_valid_last_name, fake_valid_company, fake_valid_address, fake_valid_address, Data.countries, fake_valid_state, fake_valid_city, fake_valid_zipcode, fake_valid_mobile_number)
        self.signup_page.click_create_acc_btn()
        self.acc_created_page.click_continue_btn()
        self.home_page.click_logout_btn()
        self.home_page.click_home_btn()
        
        self.home_page.check_home_page()
        self.home_page.click_signup_login_btn()
        self.login_page.check_login_header()
        self.login_page.fill_login_form(stored_valid_email, stored_valid_password)
        self.login_page.click_login_btn()
        self.home_page.check_loggedin_as_username_text(stored_valid_name)
        self.home_page.click_logout_btn()
        self.login_page.check_login_header()

        take_screenshot(self.page, "logout")