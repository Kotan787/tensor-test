import os
import re

from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator

class SabyDownloadPage(BasePage):
    def get_filename_from_href(self):
        download_link = self.find_element(Locator.download_file)
        return download_link.get_attribute("href").split('/')[-1]

    def get_filesize(self):
        download_link = self.find_element(Locator.download_file)
        return float(re.search(r"(\d+\.\d+) МБ", download_link.text).group(1))

    def click_download_file(self,download_dir):

        full_path = os.path.join(download_dir, self.get_filename_from_href())
        if os.path.exists(full_path):
            os.remove(full_path)
        self.click(Locator.download_file)
        self.wait.until(
            lambda d: os.path.exists(full_path) and os.path.getsize(full_path) > 0
        )
        print('файл успешно скачан')

    def check_file_size(self,download_dir):
        full_path = os.path.join(download_dir, self.get_filename_from_href())
        if os.path.exists(full_path):
            downloaded_file_size_mb = round(os.path.getsize(full_path) / (1024 * 1024),2)
            assert downloaded_file_size_mb == self.get_filesize()
            print('Размер скачанного файла ('+str(downloaded_file_size_mb)+') совпадает с указанным на сайте ('+str(self.get_filesize())+')')
            os.remove(full_path)
        else:
            raise FileExistsError