from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ComputersPage(BasePage):
    DESKTOPS = (By.LINK_TEXT, "Desktops")

    def go_to_desktops(self):
        self.click(self.DESKTOPS)

    def select_product(self, product_name):
        locator = (By.LINK_TEXT, product_name)
        self.click(locator)