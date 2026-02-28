from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_LINK = (By.LINK_TEXT, "14.1-inch Laptop")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-31")
    SUCCESS_BAR = (By.CLASS_NAME, "content")

    def open_home_page(self):
        self.driver.get("https://demowebshop.tricentis.com")

    def select_product(self):
        self.click(self.PRODUCT_LINK)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_BAR)
        ).text