from time import sleep

from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import date


class Calender(Base):


    def calender(self,product):
        self.send_text_to_textfield(date.search_locator,product)
        self.click_on_element(date.search_btn)
        self.click_on_element(date.product_link)
        self.select_a_date("April 2026")
        sleep(3)
        self.select_previous_date("April 2022")
        sleep(3)