import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage

from utils.test_data import Data
from utils.tools import *

product_name = Data.product_name
stored_product_name = product_name

class TestProducts:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = ProductsPage(self.page)
        self.product_detail_page = ProductDetailPage(self.page)

    @pytest.mark.test_products_and_details
    def test_test_products_and_details(self, test_setup):
        """Test to verify all products and product detail page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.check_home_page()
        self.home_page.click_products_btn()
        self.products_page.check_products_header()
        self.products_page.check_products_list()
        self.products_page.click_view_product()
        self.product_detail_page.check_product_info()
        self.product_detail_page.check_product_detail()

        take_screenshot(self.page, "contact_form")

    @pytest.mark.test_products_search
    def test_test_products_search(self, test_setup):
        """Test to verify the products search functionality

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.home_page.check_home_page()
        self.home_page.click_products_btn()
        self.products_page.check_products_header()
        self.products_page.check_products_list()
        self.products_page.fill_search_field(product_name)
        self.products_page.click_search_btn()
        self.products_page.check_searched_products_header()
        self.products_page.check_searched_products(stored_product_name)

        take_screenshot(self.page, "test_products_search")
        