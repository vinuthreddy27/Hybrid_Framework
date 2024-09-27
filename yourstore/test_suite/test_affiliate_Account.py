from yourstore.POM.loginpage import LogIn
from yourstore.POM.register_affiliate_accountpage import Affiliate_account

def test_affiliateaccount(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com",
                                      "selenium")

    affiliate_po=Affiliate_account(driver)
    affiliate_po.affiliate_account("Demowebshop",
                                   "https://demowebshop.com",
                                   "9148593989",
                                   "paypal@gmail.com")

    assert driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']").is_displayed()