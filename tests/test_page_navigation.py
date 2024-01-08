import pytest
from pages.home_page import HomePage
from pages.list_test_cases_page import ListTestCasesPage

from utils.tools import *

class TestPageNavigation:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.test_cases_page = ListTestCasesPage(self.page)

    @pytest.mark.test_cases_page
    def test_test_cases_page(self, test_setup):
        """Test to verify the test cases page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.check_home_page()
        self.test_cases_page.click_test_cases_btn()
        self.test_cases_page.check_test_cases_header()

        take_screenshot(self.page, "test_cases_page")