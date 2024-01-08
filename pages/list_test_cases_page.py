from playwright.sync_api import Page
from pages.base_page import BasePage

class ListTestCasesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__test_cases_btn = '(//a[@class="test_cases_list"]//button[@class="btn btn-success"])[1]'
        self.__test_cases_header = '//b[text()="Test Cases"]'

    def click_test_cases_btn(self) -> None:
        self.click_element(self.__test_cases_btn)

    def check_test_cases_header(self) -> None:
        self.is_element_visible(self.__test_cases_header)