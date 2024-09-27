from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import LoginPage_locators

class LogIn(Base):
    def login_to_the_application(self,email,password):
        self.click_on_element(LoginPage_locators.my_account_locator)
        self.click_on_element(LoginPage_locators.login_locator)
        self.send_text_to_textfield(LoginPage_locators.email_locator,email)
        self.send_text_to_textfield(LoginPage_locators.password_locator,password)
        self.Submit(LoginPage_locators.password_locator)
        # self.click_on_element(LoginPage_locators.login_btn)
