import allure
from allure_commons.types import AttachmentType

from yourstore.POM.passwordchange_page import ChangePassword


def test_change_password(driver):
    password_page_obj=ChangePassword(driver)
    password_page_obj.login_and_changepassowrd("reddyvinuth27@gmail.com",
                                               "selenium",
                                               "selenium",
                                               "selenium")

    condition=driver.find_element("xpath","//div[@id='content']/.//p").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_change_password.png",
                      attachment_type=AttachmentType.PNG)
