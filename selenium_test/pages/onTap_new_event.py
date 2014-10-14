from onTap_base import onTap
from selenium_test.base.webObjects import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class onTapNewEvent(onTap):

    event_style_loc = "select#event_event_style"
    event_style_by = "css"

    event_title_loc = "input#event_title"
    event_title_by = "css"

    event_description_loc = "input#event_description"
    event_description_by = "css"

    add_host_loc = "button#add-event-host"
    add_host_by = "css"

    add_host_select_loc = "select#event_hosts"
    add_host_select_by = "css"

    event_url_loc = "input#event_url"
    event_url_by = 'css'

    event_host_loc = "input#event_host"
    event_host_by = 'css'

    add_go_to_meeting_loc = "label[for=event_has_GoToMeeting]"
    add_go_to_meeting_by = "css"

    meeting_url_loc = "input#event_go_to_meeting_url"
    meeting_url_by = "css"

    meeting_phone_loc = "input#event_meeting_phone_number"
    meeting_phone_by = "css"

    meeting_access_code_loc = "input#event_access_code"
    meeting_access_code_by = "css"

    event_date_loc = "input#datepicker"
    event_date_by = "css"

    event_date_label_loc = "label[for=event_event_date]"
    event_date_label_by = "css"

    event_title_label_loc = "label[for=event_title]"
    event_title_label_by = "css"

    event_start_loc = "label[for=event_event_time] ~ select"
    event_start_by = "css"

    event_end_loc = "label[for=event_end_time] ~ select"
    event_end_by = "css"

    restricted_loc = "label[for=event_restricted]"
    restricted_by = "css"

    submit_button_loc = "input.btn.btn-primary[type=submit]"
    submit_button_by = "css"

    def event_style(self):
        return webSelect(self.driver, self.event_style_by, self.event_style_loc)

    def event_title(self):
        return webEdit(self.driver, self.event_title_by, self.event_title_loc)

    def event_description(self):
        return webEdit(self.driver, self.event_description_by, self.event_description_loc)

    def add_host_button(self):
        return webButton(self.driver, self.add_host_by, self.add_host_loc)

    def add_host_select(self):
        return webSelect(self.driver, self.add_host_select_by, self.add_host_select_loc)

    def event_url(self):
        return webEdit(self.driver, self.event_url_by, self.event_url_loc)

    def event_host(self):
        return webEdit(self.driver, self.event_host_by, self.event_host_loc)

    def has_go_to_meeting(self):
        #Need to implement webCheck
        #return webCheck(self.driver, self.add_go_to_meeting_by, self.add_go_to_meeting_loc)
        return webElement(self.driver, self.add_go_to_meeting_by, self.add_go_to_meeting_loc)

    def meeting_url(self):
        return webEdit(self.driver, self.meeting_url_by, self.meeting_url_loc)

    def meeting_phone_number(self):
        return webEdit(self.driver, self.meeting_phone_by, self.meeting_phone_loc)

    def meeting_access_code(self):
        return webEdit(self.driver, self.meeting_access_code_by, self.meeting_access_code_loc)

    def event_date(self):
        return webEdit(self.driver, self.event_date_by, self.event_date_loc)

    def event_date_label(self):
        return webElement(self.driver, self.event_date_label_by, self.event_date_label_loc)

    def event_title_label(self):
        return webElement(self.driver, self.event_title_label_by, self.event_title_label_loc)

    def event_start_time(self):
        return webSelect(self.driver, self.event_start_by, self.event_start_loc)

    def event_end_time(self):
        return webSelect(self.driver, self.event_end_by, self.event_end_loc)

    def event_restricted(self):
        #Need to implement webCheck
        #return webCheck(self.driver, self.restricted_by, self.restricted_loc)
        return webElement(self.driver, self.restricted_by, self.restricted_loc)

    def submit_button(self):
        return webButton(self.driver, self.submit_button_by, self.submit_button_loc)


    def set_event_date(self, date):
        self.event_date().set(date)

        #wait = WebDriverWait(self, 10)
        #element = wait.until(EC.element_to_be_clickable((self.event_date_label_by, self.event_date_label_loc)))
        self.event_title_label().click()

    def submit_is_visible(self):
        wait = WebDriverWait(self, 10)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Create Event')))


    def fill_form(self, data):
        for key, value in data.iteritems():
            if key == 'has_go_to_meeting':
                getattr(self, key)().click()
                time.sleep(0.1)
            elif key == 'set_event_date':
                getattr(self, key)(value)
            elif key == 'event_style':
                getattr(self, 'event_style')().set(value)
                time.sleep(0.25)
            elif value == 'click':
                getattr(self, key)().click()
            else:
                getattr(self, key)().set(value)


