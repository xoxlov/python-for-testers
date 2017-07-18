# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Maxim", last_name="Pichugin",
                      work_phone="+7.111.111.1111",
                      position="Main Boss", company="Cherehapa Ltd.",
                      address_1="Moscow", email="email@mail.me")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    # new list is made of old list with new item added
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    # new empty contact has been added to the list
    old_contacts.append(Contact())
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
