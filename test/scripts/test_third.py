import os
from time import sleep

from src.page_object.pages.saby_download_page import SabyDownloadPage
from src.page_object.pages.saby_main_page import SabyMainPage

def test_second(driver):

    download_dir = os.path.join(os.getcwd(),'test','scripts')

    main_page = SabyMainPage(driver)
    main_page.driver.get("https://saby.ru")
    main_page.click_download()

    download_page = SabyDownloadPage(driver)
    download_page.click_download_file(download_dir)
    download_page.check_file_size(download_dir)
