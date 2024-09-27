# from time import sleep
#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.select import Select
#
# driver=WebDriver()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# driver.switch_to.frame("frame-one796456169")
# driver.find_element("xpath","//span[@class='icon_calendar']").click()
# select=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
# s1=Select(select)
# s1.select_by_value("1924")
# sleep(3)

from time import sleep
# from selenium.webdriver.chrome.webdriver import WebDriver
#
# driver=WebDriver()
# driver.get("https://www.dezlearn.com/nested-iframes-example/")
# driver.maximize_window()
#
# driver.switch_to.frame("parent_iframe")
# driver.switch_to.frame("iframe1")
# iframe2_btn=driver.find_element("id","u_5_6")
# iframe2_btn.click()
#
# sleep(7)


# from selenium.webdriver.chrome.webdriver import WebDriver

# driver=WebDriver()
# driver.maximize_window()
# driver.get("https://demoapps.qspiders.com/ui/frames?sublist=0")
#
# frame=driver.find_element("xpath","//iframe[@class='w-full h-96']")
# driver.switch_to.frame(frame)

# username_tf=driver.find_element("id","username")
# username_tf.clear()
# username_tf.send_keys("Admin")
#
# password_tf=driver.find_element("id","password")
# password_tf.clear()
# password_tf.send_keys("Admin@1234")
# password_tf.submit()
#
# sleep(7)


from selenium.webdriver.chrome.webdriver import WebDriver

driver=WebDriver()
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/frames/multiple?sublist=2")

sleep(5)

frame1=driver.find_element("xpath","//iframe[@class='w-full h-96'])[1]")

driver.switch_to.frame(frame1)

email=driver.find_element("id","email")
email.clear()
email.send_keys("admin@gmail.com")

password=driver.find_element("id","password")
password.clear()
password.send_keys("admin@1234")
password.submit()

sleep(7)