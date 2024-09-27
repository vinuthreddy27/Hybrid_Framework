from time import sleep

from yourstore.library.library import Base
from yourstore.utilities.locatorsHub import Add_review_for_product


class Review(Base):

    def review(self,product,name,review):
        self.send_text_to_textfield(Add_review_for_product.search_locator,product)
        self.click_on_element(Add_review_for_product.search_btn)
        sleep(3)
        self.click_on_element(Add_review_for_product.product_link)
        sleep(2)
        self.click_on_element(Add_review_for_product.image1)
        sleep(2)
        self.click_on_element(Add_review_for_product.next_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.next_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.next_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.prev_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.next_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.next_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.prev_btn)
        sleep(2)
        self.click_on_element(Add_review_for_product.next_btn)
        self.click_on_element(Add_review_for_product.close_btn)

        self.click_on_element(Add_review_for_product.review_link)
        sleep(2)
        self.clear_a_text(Add_review_for_product.yourname_tf)
        self.send_text_to_textfield(Add_review_for_product.yourname_tf,name)
        sleep(2)
        self.send_text_to_textfield(Add_review_for_product.text_area,review)
        sleep(2)
        self.click_on_element(Add_review_for_product.rating_rb)
        self.click_on_element(Add_review_for_product.continue_btn)
        sleep(12)



