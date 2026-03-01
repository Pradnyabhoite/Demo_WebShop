from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class GiftCardPage(BasePage):
    GIFT_CARD_LINK = (By.PARTIAL_LINK_TEXT,"Gift Cards")
    PHYSICAL_GIFT_CARD=(By.PARTIAL_LINK_TEXT,"$50 Physical Gift Card")
    REC_NAME=(By.ID,"giftcard_3_RecipientName")
    NAME=(By.ID,"giftcard_3_SenderName")
    MESSAGE=(By.ID,"giftcard_3_Message")
    ADD_TO_CART=(By.ID,"add-to-cart-button-3")
    SHOPPING_CART=(By.CSS_SELECTOR,"//span[text()='Shopping cart']")


    def click_gift_card(self):
        self.click(self.GIFT_CARD_LINK)

    def click_physical_gift_card(self):
        self.click(self.PHYSICAL_GIFT_CARD)

    def enter_recipient_name(self,rec_name):
        self.send_keys(self.REC_NAME, rec_name)

    def enter_sender_name(self,sender_name):
        self.send_keys(self.NAME, sender_name)

    def enter_message(self,message):
        self.send_keys(self.MESSAGE, message)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART)


