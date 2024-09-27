from yourstore.POM.loginpage import LogIn
from yourstore.POM.calender_page import Calender


def test_caleder(driver):
    login_po=LogIn(driver)
    login_po.login_to_the_application("reddyvinuth27@gmail.com","selenium")

    calender_po=Calender(driver)
    calender_po.calender("HP LP3065")


