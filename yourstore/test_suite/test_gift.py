import allure
from allure_commons.types import AttachmentType

from yourstore.POM.loginpage import LogIn
from yourstore.POM.giftpage import Send_gift


def test_gift(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com",
                                      "selenium")

    gift_po=Send_gift(driver)
    gift_po.send_gift("jyothithakkur",
                      "jyothithakkur03@gmail.com",
                      "vinuth reddy",
                      "reddyvinuth27@gmail.com",
                      "hey jyothi this is vinuth i just wann wish you a veryyyyyyyyyy happpy  birthday.......lots of loveeeeeee.....cant wait to witnesss the life which we both imagined just being beside me .....!"
                      ,"1")
    condition=driver.find_element("xpath","//p[contains(.,'Thank you for purchasing a gift certificate!')]").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test gift.png",
                      attachment_type=AttachmentType.PNG)

