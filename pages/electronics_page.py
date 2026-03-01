import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ElectronicsPage(BasePage):
    ELECTRONICS_LINK = (By.XPATH, "(//a[contains(text(), 'Electronics')])[3]")
    CAMERA_LINK = (By.XPATH, "(//a[@title='Show products in category Camera, photo'])[1]")
    CELLPHONES_LINK = (By.XPATH, "(//a[@title='Show products in category Cell phones'])[1]")
    CAMERA_PAGE = (By.XPATH, "//h1[.='Camera, photo']")
    ELECTRONICS_TAB = (By.XPATH, "(//a[contains(text(), 'Electronics' )])[1]")
    CAMERA_SUB_MENU = (By.XPATH, "(//a[contains(text(), 'Camera, photo')])[1]")
    SORT_DROPDOWN = (By.ID, "products-orderby")
    PRODUCT_PRICES = (By.XPATH, "//span[@class='price actual-price']")
    GRID_VIEW = (By.XPATH, "//*[@id='products-viewmode']/option[1]")
    LIST_VIEW = (By.XPATH, "//*[@id='products-viewmode']/option[2]")
    PRODUCT_TITLE = (By.XPATH, "//h2[@class='product-title']")





    def navigate_to_electronics_page(self):
        self.click(ElectronicsPage.ELECTRONICS_LINK)

    def navigate_to_camera_page(self):
        self.click(ElectronicsPage.CAMERA_LINK)

    def navigate_to_cellphone_page(self):
        self.click(ElectronicsPage.CELLPHONES_LINK)

    def is_camera_page_displayed(self):
        return "Camera, photo" in self.driver.page_source

    def is_cellphone_page_displayed(self):
        return "Cell phones" in self.driver.page_source


    def is_electronics_page_displayed(self):
        return "electronics" in self.driver.current_url

    def hover_on_electronics(self):
        self.hover(self.ELECTRONICS_TAB)

    def click_camera_photo(self):
        self.click(self.CAMERA_SUB_MENU)

    def is_camera_submenu_visible(self):
        elements = self.driver.find_elements(*self.CAMERA_SUB_MENU)
        return len(elements) > 0 and elements[0].is_displayed()

    def click_list_view(self):
        self.click(self.LIST_VIEW)

    def click_grid_view(self):
        self.click(self.GRID_VIEW)

    def is_list_view_displayed(self):
        return "list" in self.driver.current_url

    def is_grid_view_displayed(self):
        return "grid" in self.driver.current_url

    def sort_by_high_to_low(self):
        current_url = self.driver.current_url
        self.select_dropdown_by_visible_text(self.SORT_DROPDOWN, "Price: High to Low")
        self.wait.until(lambda d: d.current_url != current_url)

    def get_prices(self):
        elements = self.get_elements(self.PRODUCT_PRICES)
        prices = []
        for el in elements:
            text = el.text
            numeric_price = re.sub(r"[^\d.]", "", text)
            prices.append(float(numeric_price))
        return prices

    def is_sorted_high_to_low(self):
        prices = self.get_prices()
        print("Prices After Sorting: ", prices)
        return all (prices[i] >= prices[i+1]
                    for i in range(len(prices)- 1))

    def sort_products(self, sort_option):
        self.select_dropdown_by_visible_text(self.SORT_DROPDOWN, sort_option)
        self.get_elements(self.PRODUCT_TITLE)


    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_TITLE)
        return [el.text.strip() for el in elements]

    def is_price_sorted(self, reverse = False):
        prices = self.get_prices()
        print("Prices After Sorting: ", prices)
        return prices == sorted(prices, reverse=reverse)

    def is_name_sorted(self, reverse = False):
        names = self.get_product_names()
        print("Prices After Sorting: ", names)
        return names == sorted(names, reverse=reverse)




