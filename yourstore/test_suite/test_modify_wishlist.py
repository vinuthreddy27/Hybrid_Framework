import allure
from allure_commons.types import AttachmentType
from yourstore.POM.loginpage import LogIn
from yourstore.POM.modify_wishlist import Modify_wishlsit


def test_wishlist(driver):
    login_page_obj=LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com","selenium")

    wishlist_page_obj=Modify_wishlsit(driver)
    wishlist_page_obj.modify_wishlist("Samsung Galaxy Tab 10.1")

    condition=driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_wishlist.png",
                      attachment_type=AttachmentType.PNG)


def test_wishlist_2_cart(driver):
    login_page_obj = LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com", "selenium")

    wishlist_page_obj = Modify_wishlsit(driver)
    wishlist_page_obj.add_2_cart_from_wishlist("Samsung Galaxy Tab 10.1")

    condition=driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']/.//i[@class='fa fa-check-circle']").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_wishlist.png",
                      attachment_type=AttachmentType.PNG)


