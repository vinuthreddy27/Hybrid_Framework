from time import sleep
import pytest
from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Modify_wishlist

class Modify_wishlsit(Base):

    def modify_wishlist(self,product):
        self.send_text_to_textfield(Modify_wishlist.search_locator,product)
        self.click_on_element(Modify_wishlist.search_btn)
        self.click_on_element(Modify_wishlist.product_link)
        self.click_on_element(Modify_wishlist.wishlist_symbol)
        self.click_on_element(Modify_wishlist.modify_btn)
        self.click_on_element(Modify_wishlist.remove_btn)
        sleep(3)

    def add_2_cart_from_wishlist(self, product):
        self.send_text_to_textfield(Modify_wishlist.search_locator, product)
        self.click_on_element(Modify_wishlist.search_btn)
        self.click_on_element(Modify_wishlist.product_link)
        self.click_on_element(Modify_wishlist.wishlist_symbol)
        self.click_on_element(Modify_wishlist.modify_btn)
        self.click_on_element(Modify_wishlist.add_2_cart_btn)
        sleep(3)

