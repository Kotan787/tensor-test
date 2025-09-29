from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator

class SabyContactPage(BasePage):

    def click_logo(self):
        self.click(Locator.logo)
        self.driver.switch_to.window(self.driver.window_handles[-1])