import pytest
import allure
from utilities.logger import LogGenerator
from pages.base_page import BasePage
from pages.electronics_page import ElectronicsPage
from utilities.driver_factory import get_driver

logger = LogGenerator.loggen()
@allure.feature("Electronics")
@pytest.mark.regression
def test_electronics_page(setup):
    logger.info("Starting Electronics Page Test")
    driver = setup
    electronics_page = ElectronicsPage(driver)
    electronics_page.navigate_to_electronics_page()
    assert electronics_page.is_electronics_page_displayed()
    logger.info("Electronics Page Test Completed")


@allure.feature("Camera")
@pytest.mark.regression
def test_camera_page(setup):
    logger.info("Starting Camera Page Test")
    driver = setup
    camera_page = ElectronicsPage(driver)
    camera_page.navigate_to_electronics_page()
    camera_page.navigate_to_camera_page()
    assert camera_page.is_camera_page_displayed()
    logger.info("Camera Page Test Completed")


@allure.feature("Cell Phones")
@pytest.mark.regression
def test_cell_phone_page(setup):
    logger.info("Starting CellPhone Page Test")
    driver = setup
    cell_phone_page = ElectronicsPage(driver)
    cell_phone_page.navigate_to_electronics_page()
    cell_phone_page.navigate_to_cellphone_page()
    assert cell_phone_page.is_cellphone_page_displayed()
    logger.info("CellPhone Page Test Completed")

@allure.feature("Hovering")
@pytest.mark.regression
def test_hovering_page(setup):
    logger.info("Hovering Page Test Started")
    driver = setup
    hovering_page = ElectronicsPage(driver)
    hovering_page.hover_on_electronics()
    assert hovering_page.is_camera_submenu_visible()
    logger.info("Hovering Page Test Ended")

@allure.feature("Sorting High to Low Prices")
@pytest.mark.regression
def test_sort_high_to_low(setup):
    logger.info("Sorting High to Low Prices Started")
    driver = setup
    home = ElectronicsPage(driver)
    home.hover_on_electronics()
    home.click_camera_photo()
    home.sort_by_high_to_low()
    assert home.is_sorted_high_to_low(), "Prices are NOT sorted High to Low"
    logger.info("Sorting High to Low Prices Ended")

@allure.feature("Testing Grid And List View")
@pytest.mark.regression
def test_grid_and_list_view(setup):
    logger.info("Testing Grid And List View Started")
    home = ElectronicsPage(setup)
    home.hover_on_electronics()
    home.click_camera_photo()
    home.click_list_view()
    assert home.is_list_view_displayed()
    logger.info("Testing List View Ended")
    logger.info("Testing Grid View Started")
    home.click_grid_view()
    assert home.is_grid_view_displayed()
    logger.info("Testing Grid View Ended")


@allure.feature("Data Driven")
@pytest.mark.parametrize(
    "sort_option, check_type, reverse",
    [
        ("Price: Low to High", "price", False),
        ("Price: High to Low", "price", True),
        ("Name: A to Z", "name", False),
        ("Name: Z to A", "name", True),
    ]
)
def test_sorting_data_driven(setup, sort_option, check_type, reverse):
    logger.info("Testing Sorting Data Using Data Driven Started")
    home = ElectronicsPage(setup)
    home.hover_on_electronics()
    home.click_camera_photo()
    home.sort_products(sort_option)
    if check_type == "price":
        assert home.is_price_sorted(reverse), f"{sort_option} failed"
    else:
        assert home.is_name_sorted(reverse), f"{sort_option} failed"
    logger.info("Testing Sorting Data Using Data Driven Ended")







