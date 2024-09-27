import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


# @pytest.fixture(autouse=True)
# def driver():
#   print("browser launched")
#   driver=WebDriver()
#   driver.maximize_window()
#   driver.get("https://tutorialsninja.com/demo/")
#   yield driver
#   driver.quit()
#   print("browser closed")


@pytest.fixture(autouse=True)
def driver():
  print("browser launched")
  driver=WebDriver()
  driver.maximize_window()
  driver.get("https://tutorialsninja.com/demo/")
  yield driver
  driver.quit()
  print("browser closed")
