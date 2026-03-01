import configparser

import pytest
import allure

from utilities.logger import LogGenerator
from pages.base_page import BasePage
from pages.gift_page import GiftCardPage
from utilities.driver_factory import get_driver

logger = LogGenerator.loggen()
@allure.feature("Gift Card")
@pytest.mark.regression
def test_gift_card_page(setup):
    logger.info("Starting Gift card Page Test")
    driver = setup
    gift_page = GiftCardPage(driver)
    gift_page.click_gift_card()
    assert "gift-cards" in driver.current_url
    logger.info("gift-cards Test Completed")


@allure.feature("Physical Gift Card")
@pytest.mark.regression
def test_Physical_Gift_Card_page(setup):
    logger.info("Starting Camera Page Test")
    driver = setup
    gift_page = GiftCardPage(driver)
    gift_page.click_gift_card()
    gift_page.click_physical_gift_card()
    assert "50-physical-gift-card" in driver.current_url
    logger.info("50-physical-gift-card Page Test Completed")


@allure.feature("Physical Gift Card - add to cart")
@pytest.mark.regression
def test_Physical_Gift_Card_pagrece(setup):
    logger.info("Starting Camera Page Test")
    driver = setup
    gift_page = GiftCardPage(driver)
    gift_page.click_gift_card()
    gift_page.click_physical_gift_card()
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    gift_page.enter_recipient_name(config["common"]["rec_name"])
    gift_page.enter_sender_name(config["common"]["sender_name"])
    gift_page.enter_message(config["common"]["message"])
    gift_page.click_gift_card()
