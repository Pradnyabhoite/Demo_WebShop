import pytest
import yaml
from selenium import webdriver

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

with open("config/browsers.yaml") as f:
    browsers = yaml.safe_load(f)["browsers"]

@pytest.fixture(params=browsers)
def init_driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get(config["baseURL"])
    yield driver
    driver.quit()
