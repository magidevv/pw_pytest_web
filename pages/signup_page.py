from playwright.sync_api import Page
from pages.base_page import BasePage

import random

class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__acc_info_header = '//b[text()="Enter Account Information"]'
        self.__name_field = 'input[data-qa="name"]'
        self.__email_field = 'input[data-qa="email"]'
        self.__password_field = 'input[data-qa="password"]'
        self.__day_dropdown = 'select[data-qa="days"]'
        self.__month_dropdown = 'select[data-qa="months"]'
        self.__year_dropdown = 'select[data-qa="years"]'
        self.__newsletter_checkbox = 'input#newsletter'
        self.__offers_checkbox = 'input#optin'
        self.__first_name_field = 'input[data-qa="first_name"]'
        self.__last_name_field = 'input[data-qa="last_name"]'
        self.__company_field = 'input[data-qa="company"]'
        self.__address1_field = 'input[data-qa="address"]'
        self.__address2_field = 'input[data-qa="address2"]'
        self.__country_dropdown = 'select[data-qa="country"]'
        self.__state_field = 'input[data-qa="state"]'
        self.__city_field = 'input[data-qa="city"]'
        self.__zipcode_field = 'input[data-qa="zipcode"]'
        self.__mobile_number_field = 'input[data-qa="mobile_number"]'
        self.__create_acc_btn = 'button[data-qa="create-account"]'

    def check_acc_info_header(self) -> None:
        self.is_element_visible(self.__acc_info_header)

    def fill_acc_info_form(self, title, name, email, password) -> None:
        self.__title_radio_btn = f'input[value="{title}"]'
        self.check_element(self.__title_radio_btn)
        self.have_element_text(self.__name_field, name)
        self.have_element_text(self.__email_field, email)
        self.fill_element(self.__password_field, password)
        self.select_element_option_range(self.__day_dropdown, 1, 31)
        self.select_element_option_range(self.__month_dropdown, 1, 12)
        self.select_element_option_range(self.__year_dropdown, 1900, 2021)

    def select_newsletter_checkbox(self) -> None:
        self.check_element(self.__newsletter_checkbox)

    def select_offers_checkbox(self) -> None:
        self.check_element(self.__offers_checkbox)

    def fill_address_info_form(self, first_name, last_name, company, address, address2, countries, state, city, zipcode, mobile_number) -> None:
        self.fill_element(self.__first_name_field, first_name)
        self.fill_element(self.__last_name_field, last_name)
        self.fill_element(self.__company_field, company)
        self.fill_element(self.__address1_field, address)
        self.fill_element(self.__address2_field, address2)
        self.select_element_option_value(self.__country_dropdown, countries)
        self.fill_element(self.__state_field, state)
        self.fill_element(self.__city_field, city)
        self.fill_element(self.__zipcode_field, zipcode)
        self.fill_element(self.__mobile_number_field, mobile_number)

    def click_create_acc_btn(self) -> None:
        self.click_element(self.__create_acc_btn)