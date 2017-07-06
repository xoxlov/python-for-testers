# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = False
        self.wd = webdriver.Firefox(capabilities=caps)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_homepage_by_link(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def destroy(self):
        self.wd.quit()
