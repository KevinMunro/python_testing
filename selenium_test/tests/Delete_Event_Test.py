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

    def test_admin_can_delete_event(self):
        # Must put data in tuples to guarantee dictionary order
        data = [OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Lunch to detect2"),
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
        ))]
        for test_data in data:
            for platform in self.envs:
                yield self.admin_can_delete_event, platform, test_data

    def admin_can_delete_event(self, platform, data):
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
        NewEvent.submit_button().submit()

        Calendar = onTap_calendar.onTapCalendar(test_setup)
        assert_true(Calendar.is_success_message(), "No Success Message Displayed")
        assert_regexp_matches(Calendar.success_message(), '.*Event "' + data['event_title'] + '" was created.*',
                              'Success Message did not display correct event')

        assert_true(Calendar.find_event_by_title(data['event_title']), "does not exist")
        Calendar.delete_event(data['event_title'])
        assert_true(Calendar.is_error_message(), "No Error Message Displayed")
        assert_regexp_matches(Calendar.error_message(), '.*Event "' + data['event_title'] + '" was deleted*',
                              'Deletion Message did not display correct event')
        
    def test_host_cannot_delete_event(self):
        # Must put data in tuples to guarantee dictionary order
        data = [OrderedDict((
            ('event_style', "Lunch And Learn"),
            ('event_title', "Lunch to Not Delete"),
            ('event_description', "Some Description that is longer than the title, but not war and peace long"),
            ('add_host_button', 'click'),
            ('add_host_select', 'Elise Collier'),
            ('has_go_to_meeting', 'click'),
            ('meeting_url', 'http://www.google.com'),
            ('meeting_phone_number', '(336)259-7240'),
            ('meeting_access_code', '123-123-123'),
            ('set_event_date', '12/05/2014'),
            ('event_start_time', '12:00pm'),
            ('event_end_time', '1:00pm'),
            ('event_restricted', 'click')
        ))]
        for test_data in data:
            for platform in self.envs:
                yield self.admin_can_delete_event, platform, test_data

    def host_cannot_delete_event(self, platform, data):
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
        NewEvent.submit_button().submit()

        Calendar = onTap_calendar.onTapCalendar(test_setup)
        assert_true(Calendar.is_success_message(), "No Success Message Displayed")
        assert_regexp_matches(Calendar.success_message(), '.*Event "' + data['event_title'] + '" was created.*',
                              'Success Message did not display correct event')

        assert_true(Calendar.find_event_by_title(data['event_title']), "does not exist")
        Calendar.logout()
        Login.login("Random.Random", "1234")
        assert_false(Calendar.is_delete_button_present(data['event_title']))
    


