import nose
from nose.tools import assert_equal, assert_true, assert_regexp_matches
from selenium_test.base import *
from selenium_test.pages import *
from collections import OrderedDict
import time
from selenium.webdriver.common.keys import Keys


class test_Add_Event(base_test.test):

    _multiprocess_can_split_ = True
    run_locally = True

    envs = ['chrome', 'ie', 'firefox']

    def test_admin_can_add_event(self):
        # Must put data in tuples to guarantee dictionary order
        data = [OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Some Lunch and Learn"),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('has_go_to_meeting', 'click'),
            ('meeting_url', 'http://www.google.com'),
            ('meeting_phone_number', '(336)259-7240'),
            ('meeting_access_code', '123-123-123'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm'),
            ('event_restricted', 'click')
        )), OrderedDict((
            ('event_style', "Webinar"),
            ('event_title', "Some Webinar"),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('event_url', 'https://www.google.com'),
            ('event_host', 'Google'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm'),
            ('event_restricted', 'click')
        ))]
        for test_data in data:
            for platform in self.envs:
                yield self.admin_can_add_event, platform, test_data

    def admin_can_add_event(self, platform, data):
        self.driver = self.getDriver(platform, self.run_locally)
        test_setup = {
            'driver': self.driver,
            'timeout': 5
        }

        Login = onTap_login.onTapLogin(test_setup)
        Login.goto("http://localhost:3000/")
        Login.login("Company.Admin", "1234")

        Login.add_new_event()

        NewEvent = onTap_new_event.onTapNewEvent(test_setup)
        NewEvent.fill_form(data)
        NewEvent.submit_button().click()

        Calendar = onTap_calendar.onTapCalendar(test_setup)
        assert_true(Calendar.is_success_message(), "No Success Message Displayed")
        assert_regexp_matches(Calendar.success_message(), '.*Event "' + data['event_title'] + '" was created.*',
                              'Success Message did not display correct event')

        assert_true(Calendar.find_event_by_title(data['event_title']), "does not exist")
        Calendar.find_event_by_title(data['event_title'], 'details')

    def test_admin_can_not_add_event(self):
        data = [OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', ""),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm')
        )), OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Some Lunch and Learn"),
            ('event_description', ""),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm')
        )), OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Some Lunch and Learn"),
            ('event_description', ""),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('set_event_date', ''),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm')
        )), OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Some Lunch and Learn"),
            ('event_description', ""),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', ''),
            ('event_end_time', '1:00pm')
        )), OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Some Lunch and Learn"),
            ('event_description', ""),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '')
        )), OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Some Lunch and Learn"),
            ('event_description', ""),
            ('add_host_button', 'click'),
            ('add_host_select', 'Matt Watson'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '11:00am')
        )), OrderedDict((
            ('event_style', "Webinar"),
            ('event_title', ""),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('event_url', 'https://www.google.com'),
            ('event_host', 'Google'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm')
        )), OrderedDict((
            ('event_style', "Webinar"),
            ('event_title', "Some Webinar"),
            ('event_description', ""),
            ('event_url', 'https://www.google.com'),
            ('event_host', 'Google'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm')
        )),  OrderedDict((
            ('event_style', "Webinar"),
            ('event_title', "Some Webinar"),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('event_url', 'https://www.google.com'),
            ('event_host', 'Google'),
            ('set_event_date', ''),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm')
        )), OrderedDict((
            ('event_style', "Webinar"),
            ('event_title', "Some Webinar"),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('event_url', 'https://www.google.com'),
            ('event_host', 'Google'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', ''),
            ('event_end_time', '1:00pm')
        )),  OrderedDict((
            ('event_style', "Webinar"),
            ('event_title', "Some Webinar"),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('event_url', 'https://www.google.com'),
            ('event_host', 'Google'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '')
        ))]
        for test_data in data:
            for platform in self.envs:
                yield self.admin_can_not_add_event, platform, test_data

    def admin_can_not_add_event(self, platform, data):
        self.driver = self.getDriver(platform, self.run_locally)
        test_setup = {
            'driver': self.driver,
            'timeout': 25
        }

        Login = onTap_login.onTapLogin(test_setup)
        Login.goto("http://localhost:3000/")
        Login.login("Company.Admin", "1234")

        Login.add_new_event()

        NewEvent = onTap_new_event.onTapNewEvent(test_setup)
        NewEvent.fill_form(data)
        NewEvent.submit_button().click()
        assert len(self.driver.find_elements_by_css_selector("input:invalid")) > 0

