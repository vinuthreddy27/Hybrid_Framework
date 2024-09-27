from time import sleep
from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import affilicate_account_locators

class Affiliate_account(Base):

    def affiliate_account(self,companyname,website,tax,email):
        self.click_on_element(affilicate_account_locators.account_link)
        self.clear_a_text(affilicate_account_locators.company_text_field)
        self.send_text_to_textfield(affilicate_account_locators.company_text_field,companyname)
        self.clear_a_text(affilicate_account_locators.website_textfield)
        self.send_text_to_textfield(affilicate_account_locators.website_textfield,website)
        self.clear_a_text(affilicate_account_locators.tax_textfield)
        self.send_text_to_textfield(affilicate_account_locators.tax_textfield,tax)
        self.click_on_element(affilicate_account_locators.payment_mode_btn)
        self.send_text_to_textfield(affilicate_account_locators.paypal_textfield,email)
        sleep(3)
        self.click_on_element(affilicate_account_locators.continue_btn)
        sleep(2)
