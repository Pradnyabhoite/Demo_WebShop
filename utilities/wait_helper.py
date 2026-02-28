from selenium.webdriver.support.ui import WebDriverWait

def get_wait(driver,time=10):
    return WebDriverWait(driver,time)
    