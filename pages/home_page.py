from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    COMPUTERS = (By.LINK_TEXT, "Computers")

    def go_to_computers(self):
        self.click(self.COMPUTERS)