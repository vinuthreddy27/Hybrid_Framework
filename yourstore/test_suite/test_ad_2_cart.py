import allure
from allure_commons.types import AttachmentType
from yourstore.POM.loginpage import LogIn
from yourstore.POM.ad_2_cart_page import Add_2_cart

def test_add_2_cart(driver):
    login_page_obj=LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com","selenium")

    add_2_page_obj=Add_2_cart(driver)
    add_2_page_obj.add_2_cart("Samsung SyncMaster 941BW",3)

    expected_result=driver.find_element("xpath","//p[.='Your shopping cart is empty!']").is_displayed()

    if expected_result==False:
     allure.attach(driver.get_screenshot_as_png(),
                   name="test_add_2_cart_page.png",
                  attachment_type=AttachmentType.PNG)


