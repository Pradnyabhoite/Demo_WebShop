import os

def take_screenshot(driver, name):
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)
    driver.save_screenshot(f"{folder}/{name}.png")