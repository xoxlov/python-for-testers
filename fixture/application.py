from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = False
        self.wd = webdriver.Firefox(capabilities=caps)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def add_new_contact(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        contact_data = {
            "firstname": contact.first_name,
            "lastname": contact.last_name,
            "work": contact.work_phone,
            "title": contact.position,
            "company": contact.company,
            "address": contact.address_1,
            "email": contact.email
        }
        for key in contact_data:
            self.fill_input_data_field(key, contact_data[key])
        wd.find_element_by_name("submit").click()
        self.open_homepage_by_link()

    def fill_input_data_field(self, field_name, value):
        wd = self.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_homepage_by_link(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
