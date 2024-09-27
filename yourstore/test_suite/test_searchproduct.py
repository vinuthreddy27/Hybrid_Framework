import allure
from allure_commons.types import AttachmentType
from yourstore.POM.searchproductpage import Search_Product
from yourstore.POM.loginpage import LogIn

def test_search_valid_product(driver):
    login_page_obj=LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com","selenium")

    searchpage_obj=Search_Product(driver)
    searchpage_obj.search("IMAC")

    condition =  driver.find_element("xpath","//span[.='Add to Cart']").is_displayed()
    if condition == True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_login_with_proper_credetnials.png",
                      attachment_type=AttachmentType.PNG)

def test_search_invalid_product(driver):
    login_page_obj = LogIn(driver)
    login_page_obj.login_to_the_application("reddyvinuth27@gmail.com", "selenium")

    searchpage_obj = Search_Product(driver)
    searchpage_obj.search("Iphone 15 pro max")

    condition = driver.find_element("xpath", "//p[.='There is no product that matches the search criteria.']").is_displayed()
    if condition == True:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_login_with_proper_credetnials.png",
                      attachment_type=AttachmentType.PNG)
