# -*- coding: utf-8 -*-
from model.contact import Contact
import re


class ContactHelper():
    contact_cache = None

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if wd.find_elements_by_id("MassCB"):
            return
        wd.find_element_by_link_text("home").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self._fill_contact_data(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_homepage()
        self.contact_cache = None

    def update_contact_by_index(self, contact, index=0):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()
        self._fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

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
            self.open_contacts_page()
            entries_list = wd.find_elements_by_css_selector("tr[name='entry']")
            # reset index counter due to list of contacts has changed and we need to analyze from scratch
            index = 0
        self.return_to_homepage()
        self.contact_cache = None

    def _fill_contact_data(self, contact):
        contact_data = {
            "firstname": contact.first_name,
            "middlename": contact.middle_name,
            "lastname": contact.last_name,
            "nickname": contact.nickname,

            "company": contact.company,
            "title": contact.title,
            "address": contact.address,

            "home": contact.home_phone,
            "mobile": contact.mobile_phone,
            "work": contact.work_phone,
            "fax": contact.fax,

            "email": contact.email,
            "email2": contact.email2,
            "email3": contact.email3,
            "homepage": contact.homepage,

            "bday": contact.bd_day,
            "bmonth": contact.bd_month,
            "byear": contact.bd_year,
            "aday": contact.anniv_day,
            "amonth": contact.anniv_month,
            "ayear": contact.anniv_year,

            "address2": contact.secondary_address,
            "phone2": contact.secondary_phone,
            "notes": contact.notes
        }
        for key in contact_data:
            self._type_input_value(key, contact_data[key])

    def _type_input_value(self, location, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(location).click()
            wd.find_element_by_name(location).clear()
            wd.find_element_by_name(location).send_keys(value)

    def delete_contact_by_index(self, index=0):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("selected[]")[index].click()
        self._submit_and_confirm_user_deletion()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_css_selector("input[id='MassCB']").click()
        self._submit_and_confirm_user_deletion()
        self.return_to_homepage()
        self.contact_cache = None

    def _submit_and_confirm_user_deletion(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()

    def get_contact_list(self):
        if self.contact_cache is None:
            self.contact_cache = []
            for index in range(self.count()):
                self.contact_cache.append(self.get_contact_from_contact_list(index))
        return self.contact_cache

    def get_contact_from_contact_list(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        cells = wd.find_elements_by_css_selector("tr[name='entry']")[index].find_elements_by_css_selector("td")
        id = cells[0].find_element_by_css_selector("input").get_attribute("value")
        lname = cells[1].text or None
        fname = cells[2].text or None
        address = cells[3].text or None
        allemails = cells[4].text or None
        allphones = cells[5].text or None
        return Contact(first_name=fname, last_name=lname, id=id, address=address,
                       all_emails=allemails, all_phones=allphones)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)

        id = wd.find_element_by_name("id").get_attribute("value")
        # names will be used in linear concatenation, so if empty then set it to None
        firstname = wd.find_element_by_name("firstname").get_attribute("value") or None
        middlename = wd.find_element_by_name("middlename").get_attribute("value") or None
        lastname = wd.find_element_by_name("lastname").get_attribute("value") or None

        address = wd.find_element_by_name("address").get_attribute("value") or None
        # proceed phones on the page
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        allphones = self.merge_phones_like_on_homepage(Contact(home_phone=homephone, mobile_phone=mobilephone,
                                                               work_phone=workphone, secondary_phone=secondaryphone))
        # proceed emails on the page
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        allemails = self.merge_emails_like_on_homepage(Contact(email=email, email2=email2, email3=email3))

        return Contact(first_name=firstname, middle_name=middlename, last_name=lastname, id=id,
                       home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, secondary_phone=secondaryphone,
                       address=address, all_phones=allphones, all_emails=allemails)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        fullname = wd.find_element_by_css_selector("div#content b").text
        text = wd.find_element_by_id("content").text
        # look for predefined phone format items
        # the item can be absent on the page, so check it with 're.findall'
        homephone = re.search("H: (.*)", text).group(1) if re.findall("H: (.*)", text) else None
        workphone = re.search("W: (.*)", text).group(1) if re.findall("W: (.*)", text) else None
        mobilephone = re.search("M: (.*)", text).group(1) if re.findall("M: (.*)", text) else None
        secondaryphone = re.search("P: (.*)", text).group(1) if re.findall("P: (.*)", text) else None
        allphones = self.merge_phones_like_on_homepage(Contact(home_phone=homephone, mobile_phone=mobilephone,
                                                               work_phone=workphone, secondary_phone=secondaryphone))
        # look for predefined email format items
        allemails_search = re.findall("[\w.-]+@[\w.-]+", text)
        allemails = '\n'.join(allemails_search) if allemails_search else None

        return Contact(home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, secondary_phone=secondaryphone,
                       all_phones=allphones, all_emails=allemails, full_name=fullname)

    def merge_phones_like_on_homepage(self, contact):
        # phones may be absent, in this case return None
        phones = "\n".join(filter(lambda x: x != "",  # remove empty values from result
                                  map(lambda x: re.sub("[-(). ]", "", x),  # clear phone number from garbage
                                      filter(lambda x: x is not None,  # check if phone number is present
                                             [contact.home_phone, contact.mobile_phone,
                                              contact.work_phone, contact.secondary_phone]))))
        return phones if phones != "" else None

    def merge_emails_like_on_homepage(self, contact):
        # emails may be absent, in this case return None
        emails = "\n".join(filter(lambda x: x != "",
                                  filter(lambda x: x is not None,
                                         [contact.email, contact.email2, contact.email3])))
        return emails if emails != "" else None
