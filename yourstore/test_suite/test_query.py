from yourstore.POM.loginpage import LogIn
from yourstore.POM.query_page import Query

def test_query(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com",
                                      "selenium")

    query_po=Query(driver)
    query_po.query("i just need an addtional information of the product which is in your store ipod touch.....")

    assert driver.find_element("xpath","//div[@id='content']/..//p").is_displayed()