from selenium.webdriver.support.select import Select

class Base:

    def __init__(self,driver):
        self.driver=driver

    def search_for_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def click_on_element(self,locator):
        element=self.search_for_element(locator)
        element.click()

    def clear_a_text(self,locator):
        element=self.search_for_element(locator)
        element.clear()

    def Submit(self,locator):
        element=self.search_for_element(locator)
        element.submit()

    def send_text_to_textfield(self,locator,text):
        element=self.search_for_element(locator)
        element.send_keys(text)

    def select_a_option(self,locator1,locator2):
        select_element=self.search_for_element(locator1)
        s1=Select(select_element)
        element=self.search_for_element(locator2)
        s1.select_by_visible_text(element.text)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()


    def switch_to_frame(self,locator):
        self.driver.switch_to.frame(locator)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent()

    def navigational_command_back(self):
        self.driver.back()

    def navigational_command_forward(self):
        self.driver.forward()

    def navigational_command_refresh(self):
        self.driver.refresh()


    def select_a_date(self,month_year):
        self.driver.find_element("xpath","//i[@class='fa fa-calendar']").click()
        current=self.driver.find_element("xpath","//th[@class='picker-switch']").text

        while not (current.__eq__(month_year)):
            next_btn = self.driver.find_element("xpath", "//th[@class='next']")
            next_btn.click()
            current = self.driver.find_element("xpath", "//th[@class='picker-switch']").text

        self.driver.find_element("xpath","//td[.='11']").click()

    def select_previous_date(self, month_year):
        self.driver.find_element("xpath", "//i[@class='fa fa-calendar']").click()
        current = self.driver.find_element("xpath", "//th[@class='picker-switch']").text

        while not (current.__eq__(month_year)):
            next_btn = self.driver.find_element("xpath", "//th[@class='prev']")
            next_btn.click()
            current = self.driver.find_element("xpath", "//th[@class='picker-switch']").text

        self.driver.find_element("xpath", "//td[.='11']").click()



    def switch_window(self):
        parent_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles

        for handle in all_handles:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                break
        self.driver.switch_to.window(parent_window)



