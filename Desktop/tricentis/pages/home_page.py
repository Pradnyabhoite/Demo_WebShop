from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    WISHLIST_LINK = (By.CLASS_NAME, "ico-wishlist")

    def click_login(self):
        self.click(self.LOGIN_LINK)

    def click_wishlist(self):
        self.click(self.WISHLIST_LINK)