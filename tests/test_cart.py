from pages.product_page import ProductPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

def test_add_product_to_cart(setup):

    driver = setup
    product = ProductPage(driver)
    cart = CartPage(driver)

    product.open_home_page()
    product.select_product()
    product.click_add_to_cart()

    assert "The product has been added" in product.get_success_message()

    cart.open_cart()
    assert "14.1-inch Laptop" in cart.get_product_name()

def test_remove_product_from_cart(setup):

    driver = setup
    product = ProductPage(driver)
    cart = CartPage(driver)

    product.open_home_page()
    product.select_product()
    product.click_add_to_cart()

    cart.open_cart()
    cart.remove_product()

    empty_msg = driver.find_element(By.CSS_SELECTOR, ".order-summary-content").text
    assert "Your Shopping Cart is empty" in empty_msg
