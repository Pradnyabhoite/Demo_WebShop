import pytest
from pages.electronics_page import ElectronicsPage
from utilities.excel_reader import ExcelReader
from utilities.logger import LogGenerator

logger = LogGenerator.loggen()
def get_sorting_data():
    excel = ExcelReader("test_data/sorting_data.xlsx", "Sorting")
    return excel.get_data()

@pytest.mark.parametrize("data", get_sorting_data())
def test_sorting_excel_driven(setup, data):
    logger.info("Testing Sorting Data Using Exel Data Driven Started")
    driver = setup
    electronics = ElectronicsPage(driver)
    electronics.hover_on_electronics()
    electronics.click_camera_photo()
    electronics.sort_products(data["sort_option"])
    electronics.get_product_names()

    if data["check_type"] == "price":
        assert electronics.is_price_sorted(data["reverse"]), f"Sorted {data['sort_option']} failed"
    else:
        assert electronics.is_name_sorted(data["reverse"]), f"Sorted {data['sort_option']} failed"
    logger.info("Testing Sorting Data Using Exel Data Driven Ended")
