from onTap_base import onTap
from selenium_test.base.webObjects import *
import time

class onTapEvent(onTap):

    event_style_loc = "div.h2.small.pull-right"
    event_style_by = "css"

    event_title_loc = "div.title"
    event_title_by = "css"

    event_description_loc = "p.jumbo-description"
    event_description_by = "css"

    host_loc = "div.jumbo-hosts-name"
    host_by = "css"

    event_url_loc = "//div[contains(text(), 'Meeting URL:')]/a"
    event_url_by = 'xpath'

    event_host_loc = "div.jumbo-hosted-by.small"
    event_host_by = 'css'

    meeting_url_loc = "div.meeting-link a"
    meeting_url_by = "css"

    meeting_phone_loc = "div.meetingphone"
    meeting_phone_by = "css"

    meeting_access_code_loc = "div.access"
    meeting_access_code_by = "css"

    event_schedule_loc = "div.jumbo-date.small"
    event_date_by = "css"


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


