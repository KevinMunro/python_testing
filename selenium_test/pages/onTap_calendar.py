from onTap_base import onTap
from selenium_test.base.webObjects import *
import time

class onTapCalendar(onTap):

    event_title_by = 'css'

    def find_event_by_title(self, title, action='exist'):
        title = self.driver.find_elements_by_xpath('//div[contains(@class, "title") and contains(text(), "' + title + '")]')
        if len(title) > 1:
            return True
        elif action == 'details':
            self.driver.find_element_by_xpath("(//div[contains(@class, 'title') and contains(text(), '" + title + "')]/../following-sibling::div/a[contains(text(), 'Details')])[1]")
        elif action == 'attend':
            self.driver.find_element_by_xpath("(//div[contains(@class, 'title') and contains(text(), '" + title + "')]/../following-sibling::div/a[contains(text(), 'Attend')])[1]")
        elif action == 'edit':
            self.driver.find_element_by_xpath("(//div[contains(@class, 'title') and contains(text(), '" + title + "')]/../following-sibling::div/a[contains(text(), 'Edit')])[1]")
        elif action == 'delete':
            self.driver.find_element_by_xpath("(//div[contains(@class, 'title') and contains(text(), '" + title + "')]/../following-sibling::div/a[contains(text(), 'Delete')])[1]")
        elif action == 'request':
            self.driver.find_element_by_xpath("(//div[contains(@class, 'title') and contains(text(), '" + title + "')]/../following-sibling::div/a[contains(text(), 'Request To Attend')])[1]")




