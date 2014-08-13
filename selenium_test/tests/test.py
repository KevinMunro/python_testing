import random
import string
import nose
from nose.tools import assert_equal, assert_true
import sys
import logging
from selenium import webdriver
from selenium_test import pages
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


class test_test1(object):
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

        #return webdriver.Firefox()
        return webdriver.Remote(
                                command_executor='http://10.238.242.50:4444/wd/hub',
                                desired_capabilities = cap
                                )

    def test_can_add_employee14(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform


    def test_can_add_employee13(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform

    def test_can_add_employee12(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform

    def test_can_add_employee11(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform


    def test_can_add_employee10(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform

    def test_can_add_employee9(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform

    def test_can_add_employee8(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform


    def test_can_add_employee7(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform

    def test_can_add_employee6(self):
        for platform in test_test1.envs:
            yield self.can_add_employee, platform

    def can_add_employee(self, browser):
        self.driver = self.getDriver(browser)
        testsetup = {
                     'driver': self.driver,
                     'timeout': 30,
                     'goto' : "http://bluesourcestaging.herokuapp.com/"
                     }

if __name__ == '__main__':
    #This code will run the test in this file.'

    module_name = sys.modules[__name__].__file__
    logging.debug("running nose for package: %s", module_name)
    result = nose.run(argv=['firefox', '--processes=15', '--process-timeout=10000', module_name, '--nologcapture'])
    #result = nose.run(argv=['firefox',module_name, '--nologcapture'])