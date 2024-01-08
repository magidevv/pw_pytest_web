from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__new_user_header = '//h2[text()="New User Signup!"]'
        self.__signup_name_field = 'input[data-qa="signup-name"]'
        self.__signup_email_field = 'input[data-qa="signup-email"]'
        self.__signup_btn = 'button[data-qa="signup-button"]'
        self.__login_header = '//h2[text()="Login to your account"]'
        self.__email_field = 'input[data-qa="login-email"]'
        self.__password_field = 'input[data-qa="login-password"]'
        self.__login_btn = 'button[data-qa="login-button"]'
        
    login_error = "Your email or password is incorrect!"
    existing_email_error = "Email Address already exist!"

    def check_new_user_header(self) -> None:
        self.is_element_visible(self.__new_user_header)

    def fill_signup_form(self, name, email) -> None:
        self.fill_element(self.__signup_name_field, name)
        self.fill_element(self.__signup_email_field, email)

    def click_signup_btn(self) -> None:
        self.click_element(self.__signup_btn)

    def check_login_header(self) -> None:
        self.is_element_visible(self.__login_header)

    def fill_login_form(self, email, password) -> None:
        self.fill_element(self.__email_field, email)
        self.fill_element(self.__password_field, password)

    def click_login_btn(self) -> None:
        self.click_element(self.__login_btn)

    def check_invalid_login_error(self, error) -> None:
        self.__invalid_login_msg = f'//p[text()="{error}"]'
        self.is_element_visible(self.__invalid_login_msg)

    def check_existing_email_error(self, error) -> None:
        self.__existing_email_msg = f'//p[text()="{error}"]'
        self.is_element_visible(self.__existing_email_msg)