from playwright.sync_api import expect
import random

class BasePage:
    def __init__(self, page):
        self.page = page

    def get_element(self, element):
        return self.page.locator(element)
    
    def get_element_text(self, element):
        return self.get_element(element).text_content()
    
    def have_element_text(self, element, value):
        return expect(self.get_element(element)).to_have_value(value)
    
    def is_element_visible(self, element):
        return expect(self.get_element(element)).to_be_visible()
    
    def are_elements_visible(self, element):
        elements = self.get_element(element).all()
        for element in elements:
            return expect(element).to_be_visible()

    def click_element(self, element):
        self.get_element(element).click()

    def fill_element(self, element, data):
        self.get_element(element).fill(data)

    def select_element_option_range(self, element, min_range, max_range):
        option = str(random.randint(min_range, max_range))
        self.get_element(element).select_option(option)

    def select_element_option_value(self, element, options):
        option = random.choice(options)
        self.get_element(element).select_option(value=option)

    def check_element(self, element):
        self.get_element(element).check()

    def upload_element(self, element, path):
        self.get_element(element).set_input_files(path)