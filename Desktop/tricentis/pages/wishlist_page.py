import pytest
from config.driver_setup import get_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


BASE_URL = "https://demowebshop.tricentis.com"
EMAIL = "your_email@example.com"
PASSWORD = "your_password"


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_add_product_to_wishlist(driver):

    driver.get(BASE_URL)

    home = HomePage(driver)
    home.click_login()

    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)

    # Navigate directly to product
    driver.get(BASE_URL + "/14-1-inch-laptop")

    product = ProductPage(driver)
    product.add_product_to_wishlist()

    home.click_wishlist()

    wishlist = WishlistPage(driver)
    assert wishlist.is_product_in_wishlist()