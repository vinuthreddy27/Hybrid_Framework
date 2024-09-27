from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Add_a_query

class Query(Base):
    def query(self,text):
        self.click_on_element(Add_a_query.contact_us_locator)
        self.send_text_to_textfield(Add_a_query.text_area_locator,text)
        self.click_on_element(Add_a_query.submit_btn)
        self.click_on_element(Add_a_query.continue_btn)
        self.click_on_element(Add_a_query.my_account_locator)
        self.click_on_element(Add_a_query.logout_btn)
