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



def test_camera_page(setup):
    logger.info("Starting Camera Page Test")
    driver = setup
    camera_page = ElectronicsPage(driver)
    camera_page.navigate_to_electronics_page()
    camera_page.navigate_to_camera_page()
    assert camera_page.is_camera_page_displayed()
    logger.info("Camera Page Test Completed")

def test_cell_phone_page(setup):
    logger.info("Starting CellPhone Page Test")
    driver = setup
    cell_phone_page = ElectronicsPage(driver)
    cell_phone_page.navigate_to_electronics_page()
    cell_phone_page.navigate_to_cellphone_page()
    assert cell_phone_page.is_cellphone_page_displayed()
    logger.info("CellPhone Page Test Completed")




