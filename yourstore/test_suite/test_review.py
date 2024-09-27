import allure
from allure_commons.types import AttachmentType
from yourstore.POM.loginpage import LogIn
from yourstore.POM.add_reviewpage import Review

def test_review(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com",
                                      "selenium")

    review_po=Review(driver)
    review_po.review("Ipod Touch",
                     "vinuth reddy",
                     "just loved the product.....Compact, sleek, and versatile; great for music and apps.")

    condition=driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test review.png",
                      attachment_type=AttachmentType.PNG)