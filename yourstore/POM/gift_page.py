from time import sleep

from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Giftpage_locators


class Send_gift(Base):

    def send_gift(self,name,email,name1,email2,message,amount):
        self.click_on_element(Giftpage_locators.gift_locator)
        self.clear_a_text(Giftpage_locators.receipient_locator)
        self.send_text_to_textfield(Giftpage_locators.receipient_locator,name)
        self.clear_a_text(Giftpage_locators.receipient_email)
        self.send_text_to_textfield(Giftpage_locators.receipient_email,email)
        self.clear_a_text(Giftpage_locators.your_name)
        self.send_text_to_textfield(Giftpage_locators.your_name,name1)
        self.clear_a_text(Giftpage_locators.your_email)
        self.send_text_to_textfield(Giftpage_locators.your_email,email2)
        sleep(2)
        self.clear_a_text(Giftpage_locators.messeage)
        self.send_text_to_textfield(Giftpage_locators.messeage,message)
        self.click_on_element(Giftpage_locators.birthday_btn)
        self.clear_a_text(Giftpage_locators.amount)
        self.send_text_to_textfield(Giftpage_locators.amount,amount)
        self.click_on_element(Giftpage_locators.agree_checkbox)
        self.click_on_element(Giftpage_locators.continue_btn)
