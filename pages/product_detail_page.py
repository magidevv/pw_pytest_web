from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__product_info = 'div.product-information'
        self.__product_name = 'div.product-information h2'
        self.__product_category = '//p[contains(text(), "Category: ")]'
        self.__product_price = '//span[contains(text(), "Rs. ")]'
        self.__product_availability = '//b[contains(text(), "Availability:")]'
        self.__product_condition = '//b[contains(text(), "Condition:")]'
        self.__product_brand = '//b[contains(text(), "Brand:")]'

    def check_product_info(self) -> None:
        self.is_element_visible(self.__product_info)

    def check_product_detail(self) -> None:
        self.is_element_visible(self.__product_name)
        self.is_element_visible(self.__product_category)
        self.is_element_visible(self.__product_price)
        self.is_element_visible(self.__product_availability)
        self.is_element_visible(self.__product_condition)
        self.is_element_visible(self.__product_brand)