import allure
import pytest
from allure_commons.types import AttachmentType
from yourstore.POM.compare_page import Compare
from yourstore.POM.loginpage import LogIn



def test_compare(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com",
                                      "selenium")

    search_po=Compare(driver)
    search_po.product_compare("Palm Treo Pro",
                              "Sony VAIO")

    assert driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']").is_displayed()

    # if condition==True:
    #     allure.attach(driver.get_screenshot_as_png(),
    #                   name="test_compare.png",
    #                   attachment_type=AttachmentType.PNG)



