from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import LogGenerator
import random
import string


class RegisterPage(BasePage):

    logger = LogGenerator.loggen()

    register_link = (By.LINK_TEXT, "Register")
    gender_male = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")

    success_message = (By.CLASS_NAME, "result")

    def generate_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"test_{random_string}@gmail.com"

    def register_user(self, firstname, lastname, pwd):

        self.logger.info("Starting user registration")

        self.click(self.register_link)
        self.logger.info("Clicked on Register link")

        self.click(self.gender_male)

        email_id = self.generate_email()
        self.logger.info(f"Generated Email: {email_id}")

        self.send_keys(self.first_name, firstname)
        self.send_keys(self.last_name, lastname)
        self.send_keys(self.email, email_id)
        self.send_keys(self.password, pwd)
        self.send_keys(self.confirm_password, pwd)

        self.click(self.register_button)
        self.logger.info("Clicked on Register button")

        return email_id

    def get_success_message(self):
        return self.get_text(self.success_message)