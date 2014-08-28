import nose
from nose.tools import assert_equal, assert_true
from selenium_test.base import *
from selenium_test.pages import *
import re

git 
class test_Login(base_test.test):
    _multiprocess_can_split_ = True

    envs = ['ie', 'firefox', 'chrome', 'mobile chrome']

    def tearDown(self):
        try:
            self.driver.quit()
        except:
            pass

    def test_user_can_login(self):
        for platform in self.envs:
            yield self.user_can_login, platform

    def user_can_login(self, platform):
        self.driver = self.getDriver(platform)
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto': "http://ontapstaging.herokuapp.com/"
        }

        Login = onTap_login.onTapLogin(test_setup)
        Login.login("John.Smith", "1234")
        assert_true(re.match(".*/calendar", self.driver.current_url), "page did not load")

    def test_user_can_not_login(self):
        test_data = [
            {'username': 'John', 'password': '1234'},
            {'username': '1234', 'password': '1234'},
            {'username': 'John.Smith', 'password': ''}
        ]
        for data in test_data:
            for platform in self.envs:
                yield self.user_can_not_login, platform, data

    def user_can_not_login(self, platform, data):
        self.driver = self.getDriver(platform)
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto': "http://ontapstaging.herokuapp.com/"
        }
        Login = onTap_login.onTapLogin(test_setup)
        Login.login(data['username'], data['password'])
        assert Login.is_error_message(5)




