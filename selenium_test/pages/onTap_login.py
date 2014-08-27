from onTap_base import onTap
from selenium_test.base.webObjects import *


class onTapLogin(onTap):

    username_loc = "input#login_username"
    username_by = "css"

    password_loc = "input#login_password"
    password_by = "css"

    submit_button_loc = "input.btn.btn-primary"
    submit_button_by = "css"

    def username(self):
        return webEdit(self.driver, self.username_by, self.username_loc)

    def password(self):
        return webEdit(self.driver, self.password_by, self.password_loc)

    def submit_button(self):
        return webButton(self.driver, self.submit_button_by, self.submit_button_loc)

    def login(self, username, password):
        self.username().set(username)
        self.password().set(password)
        self.submit_button().click()
