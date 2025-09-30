from src.page_object.pages.saby_contacts_page import SabyContactPage
from src.page_object.pages.saby_main_page import SabyMainPage
from src.page_object.pages.tensor_about_page import TensorAboutPage
from src.page_object.pages.tensor_home_page import TensorHomePage

def test_first(driver):

    main_page = SabyMainPage(driver)
    main_page.driver.get("https://saby.ru")

    main_page.click_contacts()
    main_page.click_office_link()

    contacts_page = SabyContactPage(driver)
    contacts_page.click_logo()

    tensor_home_page = TensorHomePage(driver)
    tensor_home_page.find_people_power()
    tensor_home_page.click_about()

    tensor_about_page = TensorAboutPage(driver)
    tensor_about_page.check_images_sizes()