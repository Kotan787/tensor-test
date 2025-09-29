from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator

class SabyMainPage(BasePage):
    def click_contacts(self):
        self.click(Locator.contacts)

    def click_office_link(self):
        self.click(Locator.offices)