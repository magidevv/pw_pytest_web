from playwright.sync_api import Page
from pages.base_page import BasePage

class DeleteAccPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__acc_deleted_header = 'h2[data-qa="account-deleted"]'
        self.__continue_btn = 'a[data-qa="continue-button"]'

    def check_acc_deleted_header(self) -> None:
        self.is_element_visible(self.__acc_deleted_header)

    def click_continue_btn(self) -> None:
        self.click_element(self.__continue_btn)