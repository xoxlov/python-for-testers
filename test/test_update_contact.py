# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name="Name to be updated", last_name="Name to be updated"))
    app.contact.update_first_contact(Contact(first_name="Alexander", last_name="Pavlov",
                                             work_phone="+7.223.322.223.322",
                                             position="System Engineer", company="Cherehapa Ltd.",
                                             address_1="Moscow", email="lup@mail.me"))


def test_update_all_empty_contacts(app):
    app.contact.update_all_empty_contacts(Contact(first_name="Andrey", last_name="Vinogradov",
                                                  work_phone="+7.777.777.7777",
                                                  position="DevOps engineer", company="Cherehapa Ltd.",
                                                  address_1="Moscow", email="devops@mail.me"))


def test_update_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name="Name to be updated", last_name="Name to be updated"))
    app.contact.update_first_contact(Contact(first_name="Alexey"))
