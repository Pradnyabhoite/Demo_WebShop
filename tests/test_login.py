from utilities.logger import LogGen
from pages.login_page import LoginPage


def test_valid_login(setup):

    logger = LogGen.loggen()
    logger.info("******** Starting Login Test ********")

    driver = setup
    login_page = LoginPage(driver)

    logger.info("Opening login page")
    login_page.open_login()

    logger.info("Entering credentials")
    login_page.login("limited@gmail.com", "Test@123")

    logger.info("Verifying logout link")
    assert login_page.is_logout_displayed()

    logger.info("******** Login Test Passed ********")