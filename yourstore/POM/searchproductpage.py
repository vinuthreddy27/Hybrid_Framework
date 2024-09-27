from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import SearchProduct_locators

class Search_Product(Base):

    def search(self,text):
        self.click_on_element(SearchProduct_locators.search_locator)
        self.clear_a_text(SearchProduct_locators.search_locator)
        self.send_text_to_textfield(SearchProduct_locators.search_locator,text)
        self.click_on_element(SearchProduct_locators.search_btn)


