from pages.base_page import BasePage

class HomePage(BasePage):
    def get_title(self):
        return self.driver.title
