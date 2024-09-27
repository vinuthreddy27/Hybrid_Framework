import allure
import pytest
from allure_commons.types import AttachmentType
from yourstore.POM.loginpage import LogIn

credentials=[("reddyvinuth7@gmail.com"," "),
             (" ","selenium"),
             (" "," "),
             ("abc@gmail.com","abc")]

@pytest.mark.parametrize("email,password",credentials)
def test_login(driver,email,password):
    login_page_obj=LogIn(driver)
    login_page_obj.login_to_the_application(email,password)

    condition = driver.find_element("xpath",
                                    "//div[.='Warning: No match for E-Mail Address and/or Password.']").is_displayed()
    if condition == True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_login_with_proper_credetnials.png",
                      attachment_type=AttachmentType.PNG)



def test_login_with_proper_credentials(driver):
    login_page_obj=LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com", "selenium")

    condition = driver.find_element("xpath", "//li[.='Change your password']").is_displayed()
    if condition == True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_login_with_proper_credetnials.png",
                      attachment_type=AttachmentType.PNG)
#