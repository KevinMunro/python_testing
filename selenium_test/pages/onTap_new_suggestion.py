from onTap_base import onTap
from selenium_test.base.webObjects import *

class onTapSuggestions(onTap):

    suggestiontitle_loc = "input#suggestion_suggestion_title.form-control"
    username_by = "css"

    suggestiondescription_loc = "input#suggestion_suggestion_description.form-control"
    password_by = "css"

    submit_button_loc = "input.btn.btn-primary"
    submit_button_by = "css"

    def title(self):
        return webEdit(self.driver, self.username_by, self.username_loc)

    def description(self):
        return webEdit(self.driver, self.password_by, self.password_loc)

    def submit_button(self):
        return webButton(self.driver, self.submit_button_by, self.submit_button_loc)

    def submit_suggestion(self, title, description):
        self.title().set(title)
        self.description().set(description)
        self.submit_button().click()
