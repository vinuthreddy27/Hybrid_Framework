from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Modify_Accountdetails


class Modify_accountdetails(Base):

    def modify_account_details(self,phno):
        self.click_on_element(Modify_Accountdetails.edit_link)
        self.clear_a_text(Modify_Accountdetails.telephone_locator)
        self.send_text_to_textfield(Modify_Accountdetails.telephone_locator,phno)
        self.click_on_element(Modify_Accountdetails.continue_btn)