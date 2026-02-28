import pytest
import configparser
import allure
from utilities.driver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def setup(request):

    browser = request.config.getoption("--browser")
    driver = get_driver(browser)

    config = configparser.ConfigParser()
    config.read("config/config.ini")
    base_url = config["common"]["base_url"]

    driver.get(base_url)

    yield driver
    driver.quit()


# Hook for Screenshot on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("setup")
        if driver:
            driver.save_screenshot("screenshots/failure.png")
            allure.attach.file(
                "screenshots/failure.png",
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )