from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")
    SEARCH_RESULT = (By.CLASS_NAME, "product-title")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_search_result(self):
        return self.get_text(self.SEARCH_RESULT)