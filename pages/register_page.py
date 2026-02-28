from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    GENDER = (By.ID,"gender-female")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_MSG = (By.CLASS_NAME, "result")

    def open_register_page(self):
        self.driver.get("https://demowebshop.tricentis.com/register")

    def register_user(self,gender, first, last, email, password):
        self.click(self.GENDER)
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.send_keys(self.CONFIRM_PASSWORD, password)
        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)






"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    REGISTER_LINK = (By.CLASS_NAME,"ico-register")
    GENDER = (By.ID,"gender-male")
    FIRSTNAME = (By.ID,"FirstName")
    LASTNAME = (By.ID,"LastName")
    EMAIL = (By.ID,"Email")
    PASSWORD = (By.ID,"Password")
    CONFIRM_PASSWORD = (By.ID,"ConfirmPassword")
    REGISTER_BUTTON = (By.ID,"register-button")
    SUCCESS_MSG = (By.CLASS_NAME,"result")

    def open_register_page(self):
        self.click(self.REGISTER_LINK)

    def register_user(self,fname,lname,email,password):
        self.click(self.GENDER)
        self.enter_text(self.FIRSTNAME,fname)
        self.enter_text(self.LASTNAME,lname)
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.PASSWORD,password)
        self.enter_text(self.CONFIRM_PASSWORD,password)
        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)
"""