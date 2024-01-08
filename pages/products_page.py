from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__products_header = '//h2[text()="All Products"]'
        self.__products_list = 'div.features_items'
        self.__view_product = '(//a[text()="View Product"])[1]'
        self.__search_field = 'input#search_product'
        self.__search_btn = 'button#submit_search'
        self.__searched_products_header = '//h2[text()="Searched Products"]'
        

    def check_products_header(self) -> None:
        self.is_element_visible(self.__products_header)

    def check_products_list(self) -> None:
        self.is_element_visible(self.__products_list)

    def click_view_product(self) -> None:
        self.click_element(self.__view_product)

    def fill_search_field(self, product_name) -> None:
        self.fill_element(self.__search_field, product_name)

    def click_search_btn(self) -> None:
        self.click_element(self.__search_btn)

    def check_searched_products_header(self) -> None:
        self.is_element_visible(self.__searched_products_header)

    def check_searched_products(self, product_name) -> None:
        self.__searched_products = f'//div[@class="productinfo text-center"]//p[contains(text(), "{product_name}")]'
        self.are_elements_visible(self.__searched_products)