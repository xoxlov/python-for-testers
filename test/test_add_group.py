# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

from model.group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except Exception as e:
        print("Exception found: {}", e)
        return False


class TestGroup(unittest.TestCase):
    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = False
        self.wd = webdriver.Firefox(capabilities=caps)
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="NewGroup", header="NewGroupHeader", footer="NewGroupFooter"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def login(self, wd, username, password):
        self.open_homepage(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        # return to the groups page
        self.open_groups_page(wd)

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
