import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from utils.config_reader import load_config

def pytest_generate_tests(metafunc):
    config = load_config()
    if "browser" in metafunc.fixturenames:
        metafunc.parametrize("browser", config["browsers"])

@pytest.fixture(scope="function")
def driver(browser):
    config = load_config()

    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()

    else:
        raise Exception("Browser not supported")

    driver.implicitly_wait(config["implicit_wait"])
    driver.get(config["base_url"])

    yield driver
    driver.quit()