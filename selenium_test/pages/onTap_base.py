from selenium_test.base import *
from selenium_test.base.webObjects import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wait


class onTap(base_page.Page):

    red_alert_loc = "div.alert.alert-danger"
    red_alert_by = "css"

    admin_drop_down_loc = "a.dropdown-toggle"
    admin_drop_down_by = "css"

    add_new_event_loc = "//ul[@class='dropdown-menu']//a[contains(., 'Add New Event')]"
    add_new_event_by = "xpath"

    add_new_suggestion_loc = "//a[contains(., 'Suggest Topics')]"
    add_new_suggestion_by = "xpath"

    def admin_drop_down(self):
        return webElement(self.driver, self.admin_drop_down_by, self.admin_drop_down_loc)

    def add_new_event_link(self):
        return webLink(self.driver, self.add_new_event_by, self.add_new_event_loc)

    def add_new_suggestion_link(self):
        return webLink(self.driver, self.add_new_suggestion_by, self.add_new_suggestion_loc)

    def is_error_message(self, timeout=0):
        self.driver.implicitly_wait(timeout)
        boolFound = len(self.driver.find_elements_by_css_selector('div.alert.alert-danger')) > 0
        self.driver.implicitly_wait(self.timeout)
        return boolFound

    def is_success_message(self, timeout=0):
        self.driver.implicitly_wait(timeout)
        boolFound = len(self.driver.find_elements_by_css_selector('div.alert.alert-success')) > 0
        self.driver.implicitly_wait(self.timeout)
        return boolFound

    def success_message(self):
        return self.driver.find_element_by_css_selector('div.alert.alert-success').text

    def add_new_event(self):
        self.admin_drop_down().click()
        self.add_new_event_link().click()

    def add_new_suggestion(self):
        self.add_new_suggestion_link().click()

