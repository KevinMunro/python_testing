import nose
from nose.tools import assert_equal, assert_true
import sys
sys.path.append('../../')
from selenium_test.pages.onTap_login import onTapLogin
from selenium_test.base.base_test import base_test
import re


class test_Login(base_test):
    _multiprocess_can_split_ = True

    envs = ['ie', 'firefox', 'chrome']

    @classmethod
    def setUpClass(self):
        pass

    def tearDown(self):
        self.driver.quit()

    def test_user_can_login(self):
        for platform in self.envs:
            yield self.user_can_login, platform

    def user_can_login(self, browser):
        self.driver = self.getDriver("chrome")
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto': "http://ontapstaging.herokuapp.com/"
        }

        Login = onTapLogin(test_setup)
        Login.login("John.Smith", "1234")
        assert_true(re.match(".*/calendar", self.driver.current_url), "page did not load")

    def test_user_can_not_login(self):
        test_data = [
            {'username': 'John', 'password': '1234'},
            {'username': '', 'password': '1234'},
            {'username': 'John.Smith', 'password': ''}
        ]
        for data in test_data:
            for platform in self.envs:
                yield self.user_can_not_login, platform, data

    def user_can_not_login(self, platform, data):
        self.driver = self.getDriver("chrome")
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto': "http://ontapstaging.herokuapp.com/"
        }
        Login = onTapLogin(test_setup)
        Login.login(data['username'], data['password'])
        assert Login.is_error_message(5)




