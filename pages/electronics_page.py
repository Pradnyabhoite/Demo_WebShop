from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ElectronicsPage(BasePage):
    ELECTRONICS_LINK = (By.XPATH, "(//a[contains(text(), 'Electronics')])[3]")
    CAMERA_LINK = (By.XPATH, "(//a[@title='Show products in category Camera, photo'])[1]")
    CELLPHONES_LINK = (By.XPATH, "(//a[@title='Show products in category Cell phones'])[1]")
    CAMERA_PAGE = (By.XPATH, "//h1[.='Camera, photo']")


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



