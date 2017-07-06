# -*- coding: utf-8 -*-


class ContactHelper():
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        self.app.open_homepage()

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self._fill_contact_data(contact)
        wd.find_element_by_name("submit").click()
        self.app.open_homepage_by_link()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first group on page if any
        contacts_list = wd.find_elements_by_name("selected[]")
        if contacts_list:
            contacts_list[0].click()
            self._submit_and_confirm_user_deletion()
        self.open_contacts_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        # find and select all contacts on page
        if wd.find_elements_by_name("selected[]"):
            wd.find_element_by_css_selector("input[id='MassCB']").click()
            self._submit_and_confirm_user_deletion()
        self.open_contacts_page()

    def _submit_and_confirm_user_deletion(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()

    def update_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        edit_buttons = wd.find_elements_by_css_selector("img[title='Edit']")
        if edit_buttons:
            edit_buttons[0].click()
            self._fill_contact_data(contact)
            wd.find_element_by_name("update").click()
            self.app.open_homepage_by_link()

    def update_all_empty_contacts(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # try to find the full list of contacts records
        entries_list = wd.find_elements_by_css_selector("tr[name='entry']")
        # if any records found then analyze them
        index = 0
        while index < len(entries_list):
            # get last and first names of contact and check if they're not empty - then continue without update
            lastname = entries_list[index].find_elements_by_css_selector("td")[1].get_property("textContent")
            firstname = entries_list[index].find_elements_by_css_selector("td")[2].get_property("textContent")
            if lastname or firstname:
                index += 1
                continue
            # contact with no name found
            entries_list[index].find_element_by_css_selector("img[title='Edit']").click()
            self._fill_contact_data(contact)
            wd.find_element_by_name("update").click()
            self.app.open_homepage_by_link()
            entries_list = wd.find_elements_by_css_selector("tr[name='entry']")
            # reset index counter due to list of contacts has changed and we need to analyze from scratch
            index = 0
        self.app.open_homepage_by_link()

    def _fill_contact_data(self, contact):
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
            self._type_input_value(key, contact_data[key])

    def _type_input_value(self, location, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(location).click()
            wd.find_element_by_name(location).clear()
            wd.find_element_by_name(location).send_keys(value)
