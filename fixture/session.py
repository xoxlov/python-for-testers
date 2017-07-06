# -*- coding: utf-8 -*-


class SessionHelper():
    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/"):
            return
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.app.wd
        self.open_homepage()
        self._type_input_value("user", username)
        self._type_input_value("pass", password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def _type_input_value(self, location, value):
        wd = self.app.wd
        wd.find_element_by_name(location).click()
        wd.find_element_by_name(location).clear()
        wd.find_element_by_name(location).send_keys(value)

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            self.logout()
        self.login(username, password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"
