from playwright.sync_api import Page
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__contact_us_header = '//h2[text()="Get In Touch"]'
        self.__name_field = 'input[data-qa="name"]'
        self.__email_field = 'input[data-qa="email"]'
        self.__subject_field = 'input[data-qa="subject"]'
        self.__message_field = 'textarea[data-qa="message"]'
        self.__upload_file = 'input[type="file"]'
        self.__submit_btn = 'input[type="submit"]'
        self.__alert_success_msg = '//div[contains(@class, "status") and contains(@class, "alert") and contains(@class, "alert-success") and text()="Success! Your details have been submitted successfully."]'
        self.__home_btn = '//span[text()=" Home"]'

    def check_contact_us_header(self) -> None:
        self.is_element_visible(self.__contact_us_header)

    def fill_contact_us_form(self, name, email, subject, message) -> None:
        self.fill_element(self.__name_field, name)
        self.fill_element(self.__email_field, email)
        self.fill_element(self.__subject_field, subject)
        self.fill_element(self.__message_field, message)

    def upload_file(self) -> None:
        file_path = 'data/test.png'
        self.upload_element(self.__upload_file, file_path)

    def click_ok_btn(self) -> None:
        def handle_dialog(dialog):
            print(f'Dialog message: {dialog.message}')
            dialog.accept()

        self.page.on('dialog', handle_dialog)
        self.click_element(self.__submit_btn)

    def check_alert_success(self) -> None:
        self.is_element_visible(self.__alert_success_msg)

    def click_home_btn(self) -> None:
        self.click_element(self.__home_btn)