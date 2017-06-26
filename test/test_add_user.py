# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

from model.contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except Exception as e:
        print("Exception found: {}", e)
        return False


class TestUser(unittest.TestCase):
    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = False
        self.wd = webdriver.Firefox(capabilities=caps)
        self.wd.implicitly_wait(60)
    
    def test_add_new_user(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact(first_name="Maxim", last_name="Pichugin",
                                         work_phone="+7.111.111.1111",
                                         position="Main Boss", company="Cherehapa Ltd.",
                                         address_1="Moscow",
                                         email="email@mail.me"))
        self.open_homepage_by_link(wd)
        self.logout(wd)

    def test_add_new_empty_user(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact())
        self.open_homepage_by_link(wd)
        self.logout(wd)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def open_homepage_by_link(self, wd):
        wd.find_element_by_link_text("home").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_data_field(wd, "firstname", contact.first_name)
        self.fill_contact_data_field(wd, "lastname", contact.last_name)
        self.fill_contact_data_field(wd, "work", contact.work_phone)
        self.fill_contact_data_field(wd, "title", contact.position)
        self.fill_contact_data_field(wd, "company", contact.company)
        self.fill_contact_data_field(wd, "address", contact.address_1)
        self.fill_contact_data_field(wd, "email", contact.email)
        wd.find_element_by_name("submit").click()

    def fill_contact_data_field(self, wd, field_name, value):
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
