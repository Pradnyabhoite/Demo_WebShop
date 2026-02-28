from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_title(self):
        return self.driver.title

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def select_dropdown_by_visible_text(self, locator, text):
        dropdown = self.wait.until(EC.presence_of_element_located(locator))
        Select(dropdown).select_by_visible_text(text)

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
