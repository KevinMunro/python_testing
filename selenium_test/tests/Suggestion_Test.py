import nose
from nose.tools import assert_equal, assert_true
from selenium_test.base import *
from selenium_test.pages import *
import re


class test_Suggestion(base_test.test):
    _multiprocess_can_split_ = True

    run_locally = True
    envs = ['firefox']

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

        Login.add_new_suggestion()

        NewSuggestion = onTap_new_suggestion.onTapNewSuggestion(test_setup)
        NewSuggestion.submit_suggestion("Java Programming", "Learn about the joys and pain of programming in java")
        assert Login.is_success_message(5)

    def test_user_can_not_submit_suggestion(self):
        test_data = [
            {'title': 'Python Programming', 'description': ''},
            {'title': '', 'description': 'Learn to program in Python'},
            {'title': '', 'description': ''}
        ]
        for data in test_data:
            for platform in self.envs:
                yield self.user_can_not_submit_suggestion, platform, data

    def user_can_not_submit_suggestion(self, platform, data):
        self.driver = self.getDriver(platform, self.run_locally)
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto': "http://ontapstaging.herokuapp.com/"
        }
        Login = onTap_login.onTapLogin(test_setup)
        Login.goto("http://ontapstaging.herokuapp.com/")
        Login.login("John.Smith", "Password")
        Login.add_new_suggestion()
        NewSuggestion = onTap_new_suggestion.onTapNewSuggestion(test_setup)
        NewSuggestion.submit_suggestion(data['title'], data['description'])
        assert len(self.driver.find_elements_by_css_selector("input:invalid")) > 0




