from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    email = (By.TAG_NAME, "input")
    
    def enter_email(self, email):
        self.wait_for_element(self.email).send_keys(email)
