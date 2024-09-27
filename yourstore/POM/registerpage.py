from time import sleep

from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import RegisterPagelocators

class Myaccount(Base):

    def register(self,firstname,lastname,email,telephone,password,conformpassword):
        self.click_on_element(RegisterPagelocators.my_account_locator)
        self.click_on_element(RegisterPagelocators.register_locator)
        self.send_text_to_textfield(RegisterPagelocators.first_name_locator,firstname)
        self.send_text_to_textfield(RegisterPagelocators.last_name_locator,lastname)
        self.send_text_to_textfield(RegisterPagelocators.email_locator,email)
        self.send_text_to_textfield(RegisterPagelocators.telephone_locator,telephone)
        self.send_text_to_textfield(RegisterPagelocators.password_locator,password)
        self.send_text_to_textfield(RegisterPagelocators.conform_password_locator,conformpassword)
        self.click_on_element(RegisterPagelocators.radio_btn)
        self.click_on_element(RegisterPagelocators.privacy_policy_check_box_btn)
        self.click_on_element(RegisterPagelocators.register_btn)
        sleep(3)

