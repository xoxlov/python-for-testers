# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Name to be deleted", last_name="Name to be deleted"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # first contact in old list was removed
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Name to be deleted", last_name="Name to be deleted"))
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    # need to check the length of new list to be 0, i.e. list is empty
    assert len(new_contacts) == 0
