from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__logo = 'div.logo.pull-left'
        self.__shop_menu = 'div.shop-menu.pull-right'
        self.__signup_login_btn = '//a[text()=" Signup / Login"]'
        self.__delete_acc_btn = '//a[text()=" Delete Account"]'
        self.__logout_btn = '//a[text()=" Logout"]'
        self.__home_btn = '//a[text()=" Home"]'
        self.__contact_us_btn = '//a[text()=" Contact us"]'
        self.__products_btn = '//a[text()=" Products"]'
        self.__subscription_header = '//h2[text()="Subscription"]'
        self.__subscribe_email_field = 'input#susbscribe_email'
        self.__subscribe_btn = 'button#subscribe'

    success_subscribe_msg = "You have been successfully subscribed!"

    def check_home_page(self) -> None:
        self.is_element_visible(self.__logo)
        self.is_element_visible(self.__shop_menu)

    def click_signup_login_btn(self) -> None:
        self.click_element(self.__signup_login_btn)

    def check_loggedin_as_username_text(self, username) -> None:
        self.__loggedin_as_username_text = f'//a[contains(text(), " Logged in as ") and contains(b, "{username}")]'
        self.is_element_visible(self.__loggedin_as_username_text)

    def click_delete_acc_btn(self) -> None:
        self.click_element(self.__delete_acc_btn)

    def click_logout_btn(self) -> None:
        self.click_element(self.__logout_btn)

    def click_home_btn(self) -> None:
        self.click_element(self.__home_btn)

    def click_contact_us_btn(self) -> None:
        self.click_element(self.__contact_us_btn)

    def click_products_btn(self) -> None:
        self.click_element(self.__products_btn)

    def check_subscription_header(self) -> None:
        self.is_element_visible(self.__subscription_header)

    def fill_subscribe_email_field(self, email) -> None:
        self.fill_element(self.__subscribe_email_field, email)

    def click_subscribe_btn(self) -> None:
        self.click_element(self.__subscribe_btn)

    def check_success_subscribe_msg(self, msg) -> None:
        self.__success_subscribe_msg = f'//div[@id="success-subscribe"]//div[contains(text(), "{msg}")]'
        self.is_element_visible(self.__success_subscribe_msg)