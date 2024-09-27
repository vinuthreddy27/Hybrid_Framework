import allure
from allure_commons.types import AttachmentType

from yourstore.POM.modify_Accountdetails  import Modify_accountdetails
from yourstore.POM.loginpage import LogIn

def test_modify_account_details(driver):
    login_page_obj=LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com","selenium")

    modify_ad_page_obj=Modify_accountdetails(driver)
    modify_ad_page_obj.modify_account_details("9148593987")

    condition=driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_modify.png",
                      attachment_type=AttachmentType.PNG)
