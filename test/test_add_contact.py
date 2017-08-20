# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.add_new(json_contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
