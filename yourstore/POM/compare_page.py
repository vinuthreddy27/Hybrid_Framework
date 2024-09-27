from time import sleep

from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import compare_page_locators

class Compare(Base):

    def product_compare(self,product,product2):
        self.send_text_to_textfield(compare_page_locators.search_locator,product)
        self.click_on_element(compare_page_locators.search_btn)
        self.click_on_element(compare_page_locators.product_locator)
        self.click_on_element(compare_page_locators.compare_btn)
        self.clear_a_text(compare_page_locators.search_locator)
        self.send_text_to_textfield(compare_page_locators.search_locator,product2)
        self.click_on_element(compare_page_locators.search_btn)
        self.click_on_element(compare_page_locators.product_locator2)
        self.click_on_element(compare_page_locators.compare_btn)
        self.navigational_command_back()
        self.click_on_element(compare_page_locators.compare_link)
        sleep(3)
        self.click_on_element(compare_page_locators.remove_btn)
        sleep(3)
        self.click_on_element(compare_page_locators.add_to_cart_btn)


