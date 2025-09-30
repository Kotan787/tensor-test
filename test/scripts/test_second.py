from time import sleep

from src.page_object.pages.saby_contacts_page import SabyContactPage
from src.page_object.pages.saby_main_page import SabyMainPage

def test_second(driver):

    main_page = SabyMainPage(driver)
    main_page.driver.get("https://saby.ru")

    main_page.click_contacts()
    main_page.click_office_link()

    contacts_page = SabyContactPage(driver)
    contacts_page.check_region('Костромская обл')
    old_partners_list = contacts_page.get_partners_list()

    contacts_page.change_region()

    contacts_page.check_region('Камчатский край')
    contacts_page.check_region_url('41-kamchatskij-kraj')
    contacts_page.check_region_title('Камчатский край')
    new_partners_list = contacts_page.get_partners_list()

    assert old_partners_list != new_partners_list or old_partners_list not in new_partners_list
