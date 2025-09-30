from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator

class SabyContactPage(BasePage):
    def click_logo(self):
        self.click(Locator.logo)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def change_region(self):
        self.click(Locator.region)
        self.click(Locator.new_region_select_link)

    def check_region(self,region):
        self.check_exists_element(Locator.region)
        assert region in self.find_element(Locator.region).text

    def check_region_url(self, region):
        assert region in self.get_current_url()

    def check_region_title(self, region):
        assert region in self.get_title()

    def get_partners_list(self):
        partners_list = self.find_elements(Locator.partners_list)
        assert partners_list
        return partners_list