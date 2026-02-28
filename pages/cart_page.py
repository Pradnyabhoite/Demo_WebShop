from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    SHOPPING_CART_LINK = (By.LINK_TEXT, "Shopping cart")
    PRODUCT_NAME = (By.CLASS_NAME, "product-name")
    REMOVE_CHECKBOX = (By.NAME, "removefromcart")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")

    def open_cart(self):
        self.click(self.SHOPPING_CART_LINK)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def remove_product(self):
        self.driver.find_element(By.NAME, "removefromcart").click()
        self.driver.find_element(By.NAME, "updatecart").click()