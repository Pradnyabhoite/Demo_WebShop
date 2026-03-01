'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser):

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser):

    browser = browser.lower()

    if browser == "chrome":

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")

        # service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome()

    elif browser == "firefox":

        # service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox()

    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    return driver