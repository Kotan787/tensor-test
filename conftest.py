import os

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    download_dir = os.path.join(os.getcwd(),'test','scripts')

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()