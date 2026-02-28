import pytest
import random
from pages.register_page import RegisterPage
from utilities.logger import LogGen

@pytest.mark.parametrize(
    "gender, first_name, last_name, password",
    [
        ("Male", "Kaliya", "Ji", "Test@123"),
        ("Female", "Basanti", "Ji", "Test@123"),
    ]
)
def test_user_registration(setup,gender, first_name, last_name, password):

    logger = LogGen.loggen()
    logger.info("******** Starting Registration Test ********")

    driver = setup
    register = RegisterPage(driver)

    random_email = f"test{random.randint(1000,9999)}@gmail.com"

    logger.info("Opening register page")
    register.open_register_page()

    logger.info("Entering registration details")
    register.register_user(
        gender,
        first_name,
        last_name,
        random_email,
        password
    )

    assert "registration completed" in register.get_success_message().lower()

    logger.info("******** Registration Test Passed ********")

    assert "registration completed" in register.get_success_message().lower()





"""
import random
import pytest
from pages.register_page import RegisterPage
from testdata.test_data import TestData

def test_user_registration(setup):
    driver = setup
    register = RegisterPage(driver)

    random_email = f"test{random.randint(1000,9999)}@gmail.com"
    register.open_register_page()
    register.register_user(
        TestData.GENDER,
        TestData.FIRST_NAME,
        TestData.LAST_NAME,
        random_email,
        "Test@123"
    )

    assert "your registration completed" in register.get_success_message().lower()
"""

