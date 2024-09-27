from time import sleep

from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Add_2_cart_locaters

class Add_2_cart(Base):

    def add_2_cart(self,text,number):
        self.clear_a_text(Add_2_cart_locaters.search_locator)
        self.send_text_to_textfield(Add_2_cart_locaters.search_locator,text)
        self.click_on_element(Add_2_cart_locaters.search_btn)
        self.click_on_element(Add_2_cart_locaters.product_locator)
        self.clear_a_text(Add_2_cart_locaters.quantity_locator)
        self.send_text_to_textfield(Add_2_cart_locaters.quantity_locator,number)
        self.click_on_element(Add_2_cart_locaters.add_to_cart_locator)
        self.click_on_element(Add_2_cart_locaters.cart_locator)
        self.click_on_element(Add_2_cart_locaters.remove_btn)
        self.click_on_element(Add_2_cart_locaters.cart_locator)
        sleep(1)

