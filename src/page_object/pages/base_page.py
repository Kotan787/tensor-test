from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))

    def click(self, locator):
        self.find_element(locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def get_elements_parent(self,element):
        return element.find_element(By.XPATH, "..")

    def find_element_in_element(self,element,locator):
        return element.find_element(By.XPATH,locator)

    def wait_text_in_element(self,locator,text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,locator), text))

    def check_exists_element(self,locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True