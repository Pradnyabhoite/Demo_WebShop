import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.driver_setup import get_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


BASE_URL = "https://demowebshop.tricentis.com"
EMAIL = "tanusaxena38@gmail.com"
PASSWORD = "Tanu@0101"


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_add_product_to_wishlist(driver):

    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)


    home = HomePage(driver)
    home.click_login()


    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)


    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ico-logout")))


    driver.get(BASE_URL + "/14-1-inch-laptop")


    product = ProductPage(driver)
    product.add_product_to_wishlist()


    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification")))


    home.click_wishlist()


    wishlist = WishlistPage(driver)

    assert wishlist.is_product_in_wishlist(), "Product not found in wishlist"