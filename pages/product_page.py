from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart-button-72")
    SHOPPING_CART = (By.LINK_TEXT, "Shopping cart")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.SHOPPING_CART)