import sys
sys.path.append('../../')
import selenium_test.base.base_page as base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wait


class onTap(base.Page):

    red_alert_loc = "div.alert.alert-danger"
    red_alert_by = "css"

    def is_error_message(self, timeout=0):
        self.driver.implicitly_wait(timeout)
        boolFound = len(self.driver.find_elements_by_css_selector('div.alert.alert-danger')) > 0
        self.driver.implicitly_wait(self.timeout)
        return boolFound
    pass
