import nose
from nose.tools import assert_equal, assert_true
from selenium_test.base import *
from selenium_test.pages import *
import re


class test_Login(base_test.test):
    _multiprocess_can_split_ = True

    run_locally = True
    envs = ['chrome', 'ie', 'firefox']

    def tearDown(self):
        try:
            self.driver.quit()
        except:
            pass

    def test_user_can_submit_suggestion(self):
        for platform in self.envs:
            yield self.user_can_submit_suggestion, platform

    def user_can_submit_suggestion(self, platform):
        self.driver = self.getDriver(platform, self.run_locally)
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30
        }

        Login = onTap_login.onTapLogin(test_setup)
        Login.goto("http://ontapstaging.herokuapp.com/")
        Login.login("John.Smith", "Password")

        Login.add_new_event()

        NewEvent = onTap_new_event.onTapNewEvent(test_setup)
        Login.login("Programming classes", "Have classes to teach the basics of programming")
        assert_true(re.match(".*/calendar", self.driver.current_url), "page did not load")

    def test_user_can_not_login(self):
        test_data = [
            {'title': 'John', 'description': '1234'},
            {'title': '', 'description': '1234'},
            {'title': 'John.Smith', 'description': ''}
        ]
        for data in test_data:
            for platform in self.envs:
                yield self.user_can_not_login, platform, data

    def user_can_not_login(self, platform, data):
        self.driver = self.getDriver(platform, self.run_locally)
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto': "http://ontapstaging.herokuapp.com/"
        }
        Login = onTap_login.onTapLogin(test_setup)
        Login.goto("http://ontapstaging.herokuapp.com/")
        Login.login(data['username'], data['password'])
        assert Login.is_error_message(5)




