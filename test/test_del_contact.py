# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Name to be deleted", last_name="Name to be deleted"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Name to be deleted", last_name="Name to be deleted"))
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
