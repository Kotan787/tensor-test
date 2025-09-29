from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator

class TensorAboutPage(BasePage):

    def check_images_sizes(self):
        images = self.find_elements(Locator.images)
        first_height = images[0].get_attribute("height")
        first_width = images[0].get_attribute("width")
        assert all(img.get_attribute("height") == first_height for img in images)
        assert all(img.get_attribute("width") == first_width for img in images)