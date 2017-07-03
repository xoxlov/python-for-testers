# -*- coding: utf-8 -*-


class ContactHelper():
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        self.app.open_homepage()

    def add_new(self, contact):
        wd = self.app.wd
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
            self._fill_input_data_field(key, contact_data[key])
        wd.find_element_by_name("submit").click()
        self.app.open_homepage_by_link()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first group on page if any
        contacts_list = wd.find_elements_by_name("selected[]")
        if (len(contacts_list)):
            contacts_list[0].click()
            # submit deletion
            wd.find_element_by_css_selector("input[value='Delete']").click()
            # confirm operation in alert
            wd.switch_to_alert().accept()
        self.open_contacts_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        # find and select all contacts on page
        if (len(wd.find_elements_by_name("selected[]"))):
            wd.find_element_by_css_selector("input[id='MassCB']").click()
            # submit deletion
            wd.find_element_by_css_selector("input[value='Delete']").click()
            # confirm operation in alert
            wd.switch_to_alert().accept()
        self.open_contacts_page()

    def _fill_input_data_field(self, field_name, value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)

