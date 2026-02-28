from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def open_login(self):
        self.driver.get("https://demowebshop.tricentis.com/login")

    def login(self, email, password):
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_logout_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.LOGOUT_LINK)
            ).is_displayed()
        except:
            return False





"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.CLASS_NAME,"ico-login")
    EMAIL = (By.ID,"Email")
    PASSWORD = (By.ID,"Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button-1.login-button")
    LOGOUT_LINK = (By.CLASS_NAME,"ico-logout")

    def open_login(self):
        self.click(self.LOGIN_LINK)

    def login(self,email,password):
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)

    def is_logout_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK)).is_displayed()
"""