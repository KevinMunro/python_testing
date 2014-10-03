from onTap_base import onTap
from selenium_test.base.webObjects import *

class onTapNewSuggestion(onTap):

    suggestiontitle_loc = "input#suggestion_suggestion_title.form-control"
    suggestiontitle_by = "css"

    suggestiondescription_loc = "input#suggestion_suggestion_description.form-control"
    suggestiondescription_by = "css"

    submit_button_loc = "input.btn.btn-primary"
    submit_button_by = "css"

    def title(self):
        return webEdit(self.driver, self.suggestiontitle_by, self.suggestiontitle_loc)

    def description(self):
        return webEdit(self.driver, self.suggestiondescription_by, self.suggestiondescription_loc)

    def submit_button(self):
        return webButton(self.driver, self.submit_button_by, self.submit_button_loc)

    def submit_suggestion(self, title, description):
        self.title().set(title)
        self.description().set(description)
        self.submit_button().click()
