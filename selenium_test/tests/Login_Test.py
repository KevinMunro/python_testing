import random
import string
import nose
from nose.tools import assert_equal, assert_true
import sys
import logging
from selenium import webdriver
import selenium_test.pages
from selenium_test import pages
from selenium_test.pages.onTap_login import onTapLogin
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import re


class test_Login(object):
    _multiprocess_can_split_ = True

    envs = ['ie', 'firefox', 'chrome']

    @classmethod
    def setUpClass(self):
        pass
    
    def tearDown(self):
        self.driver.quit()

    def getDriver(self, browser):
        if browser == "firefox":
            cap = DesiredCapabilities.FIREFOX
        if browser == "ie":
            cap = DesiredCapabilities.FIREFOX
        if browser == "chrome":
            cap = DesiredCapabilities.CHROME
        if browser == "mobile chrome":
            cap = {}
            cap['browserName'] = "Chrome"
            cap['platformName'] = "Android"
            cap['deviceName'] = ""

        return webdriver.Firefox()
        #return webdriver.Remote(
                             #   command_executor='http://10.238.242.50:4444/wd/hub',
                              #  desired_capabilities=cap
                               #)

    def test_user_can_login(self):

        for platform in self.envs:
            yield self.user_can_login, platform

    def user_can_login(self, browser):

        self.driver = self.getDriver("chrome")
        test_setup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto' : "http://ontapstaging.herokuapp.com/"
                     }

        Login = onTapLogin(test_setup)
        Login.login("Matt.Watson", "1234")
        assert_true(re.match(".*/calendar", self.driver.current_url), "page did not load")

    def test_user_can_not_login(self):
        test_data = [
            {'username': 'matt', 'password': '1234'},
            {'username': '', 'password': '1234'},
            {'username': 'matt.watson', 'password': ''}
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




