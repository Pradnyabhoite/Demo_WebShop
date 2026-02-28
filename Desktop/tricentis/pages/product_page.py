from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_WISHLIST = (By.CSS_SELECTOR, "input[value='Add to wishlist']")

    def add_product_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST)