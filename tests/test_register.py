import pytest
from pages.register_page import RegisterPage
from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


@pytest.mark.smoke
def test_register_user(setup):

    logger.info("Starting Register Test")

    driver = setup
    register = RegisterPage(driver)

    register.register_user("John", "Doe", "Password123")

    assert "Register" in driver.title

    logger.info("Register Test Completed")