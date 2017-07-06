# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Name to be deleted", last_name="Name to be deleted"))
    app.contact.delete_first_contact()


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Name to be deleted", last_name="Name to be deleted"))
    app.contact.delete_all_contacts()
