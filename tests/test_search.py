from pages.search_page import SearchPage


def test_search_product(setup):

    driver = setup
    driver.get("https://demowebshop.tricentis.com")

    search = SearchPage(driver)
    search.search_product("Laptop")

    assert "Laptop" in search.get_search_result()