from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    SEARCH_BOX = (By.ID,"small-searchterms")
    SEARCH_BUTTON = (By.CLASS_NAME,"small-searchterms")
    FIRST_PRODUCT = (By.CSS_SELECTOR,".product-item h2 a")

    def search_product(self,product_name):
        self.enter_text(self.SEARCH_BOX,product_name)
        self.click(self.SEARCH_BUTTON)

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)