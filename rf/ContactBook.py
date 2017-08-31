# -*- coding: utf-8 -*-
import json
import os.path
from fixture.application import Application
from fixture.orm import ORMFixture
from model.contact import Contact


class ContactBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_name) as config_file:
            self.target = json.load(config_file)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target["db"]
        self.dbfixture = ORMFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_contact(self, firstname, lastname):
        return Contact(first_name=firstname, last_name=lastname)

    def create_contact(self, contact):
        self.fixture.contact.add_new(contact)

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def update_contact(self, contact_old, contact_new):
        self.fixture.contact.update_contact_by_id(contact_new, contact_old.id)

    def update_value_in_list(self, contact_list, contact_to_update, contact_with_new_data):
        # NOTE: this action is based on the shallow copying of the objects and greatly on immutability
        contact = contact_list[contact_list.index(contact_to_update)]
        contact.first_name = contact_with_new_data.first_name
        contact.last_name = contact_with_new_data.last_name
