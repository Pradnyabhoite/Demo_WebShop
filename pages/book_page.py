from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookPage(BasePage):

    books_menu = (By.LINK_TEXT, "Books")
    add_to_cart = (By.XPATH, "(//input[@value='Add to cart'])[1]")
    cart_link = (By.LINK_TEXT, "Shopping cart")

    def add_book(self):
        self.click(self.books_menu)
        self.click(self.add_to_cart)
        self.click(self.cart_link)