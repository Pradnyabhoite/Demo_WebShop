import pytest
import allure
from pages.book_page import BookPage


@allure.feature("Book Module")
@pytest.mark.regression
def test_add_book_to_cart(setup):

    driver = setup
    book = BookPage(driver)

    book.add_book()

    assert "Shopping Cart" in driver.title