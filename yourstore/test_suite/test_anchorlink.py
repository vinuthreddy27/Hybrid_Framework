from yourstore.POM.loginpage import LogIn
from yourstore.POM.multiple_element import Multiple

def test_anchor(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com",
                                      "selenium")

    multiple_element_po=Multiple(driver)
    multiple_element_po.links()



