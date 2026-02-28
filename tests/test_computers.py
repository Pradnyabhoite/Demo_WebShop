from pages.home_page import HomePage
from pages.computers_page import ComputersPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_computers_end_to_end(driver):
    home = HomePage(driver)
    home.go_to_computers()

    computers = ComputersPage(driver)
    computers.go_to_desktops()
    computers.select_product("Build your own computer")

    product = ProductPage(driver)
    product.add_to_cart()
    product.go_to_cart()

    cart = CartPage(driver)

    assert "Shopping cart" in cart.get_cart_title()
