from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_first():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://saby.ru")

    contacts_xpath = '//*[contains(text(), "Контакты") and contains(@class, "sbisru-Header__menu-link")]'

    contacts = WebDriverWait(driver, 500).until(
        EC.visibility_of_element_located((By.XPATH, contacts_xpath))
    )
    contacts.click()

    office_link = '//a[contains(@href, "/contacts") and contains(@class, "sbisru-link sbis_ru-link")]'
    offices = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, office_link))
    )
    offices.click()

    logo_xpath = '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, logo_xpath))
    )
    logo.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])

    people_power_block = WebDriverWait(driver, 500).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Сила в людях')]"))
    )
    assert people_power_block.is_enabled()

    parent = people_power_block.find_element(By.XPATH, "..")
    about = parent.find_element(By.XPATH, "//a[contains(@href, '/about') and contains(.//text(), 'Подробнее') and contains(@class,'tensor_ru-link tensor_ru-Index__link')]")
    about.click()
    assert driver.current_url == 'https://tensor.ru/about'

    pictures = driver.find_elements(By.XPATH,"//*[contains(@class,'tensor_ru-About__block3-image-wrapper')]")
    first_height = pictures[0].get_attribute("height")
    assert all(img.get_attribute("height") == first_height for img in pictures)

    first_width = pictures[0].get_attribute("width")
    assert all(img.get_attribute("width") == first_width for img in pictures)
