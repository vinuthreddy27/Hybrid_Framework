from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Password_change

class ChangePassword(Base):

    def login_and_changepassowrd(self, email, password,_password,con_password):
        self.click_on_element(Password_change.my_account_locator)
        self.click_on_element(Password_change.login_locator)
        self.send_text_to_textfield(Password_change.email_locator, email)
        self.send_text_to_textfield(Password_change.password_locator, password)
        self.click_on_element(Password_change.login_btn)
        self.click_on_element(Password_change.changepassowrd_locator)
        self.send_text_to_textfield(Password_change.password,_password)
        self.send_text_to_textfield(Password_change.c_password,con_password)
        self.click_on_element(Password_change.conform_btn)
        self.click_on_element(Password_change.my_account_locator)
        self.click_on_element(Password_change.logout_btn)

