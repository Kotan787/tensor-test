from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator

class TensorHomePage(BasePage):
    ABOUT_URL = 'https://tensor.ru/about'

    def find_people_power(self):
        assert self.check_exists_element(Locator.people_power)
        self.people_power_block = self.find_element(Locator.people_power)


    def click_about(self):
        block_parent = self.get_elements_parent(self.people_power_block)
        about_link = self.find_element_in_element(block_parent,Locator.about)
        about_link.click()
        assert self.get_current_url() == self.ABOUT_URL