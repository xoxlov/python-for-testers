# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_update_random_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name="Name to be updated", last_name="Name to be updated"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    # create new Contact object with data for update
    contact = Contact(first_name="Alexander", last_name="Pavlov",
                      work_phone="+7.223.322.223.322",
                      position="System Engineer", company="Cherehapa Ltd.",
                      address_1="Moscow", email="lup@mail.me")
    # set object id to the contact id by index
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # change contact by index to the new object, id has been kept
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_all_empty_contacts(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.update_all_empty_contacts(Contact(first_name="Andrey", last_name="Vinogradov",
                                                  work_phone="+7.777.777.7777",
                                                  position="DevOps engineer", company="Cherehapa Ltd.",
                                                  address_1="Moscow", email="devops@mail.me"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # go through the contacts list and look for empty contacts
    for i in range(len(old_contacts)):
        if old_contacts[i].last_name == '' and old_contacts[i].first_name == '':
            # if the empty contact found - create new Contact object with data for update
            # object should be new every time to escape redefinition with shared pointer
            contact = Contact(first_name="Andrey", last_name="Vinogradov",
                         work_phone="+7.777.777.7777",
                         position="DevOps engineer", company="Cherehapa Ltd.",
                         address_1="Moscow", email="devops@mail.me")
            # set id for updated group
            contact.id = old_contacts[i].id
            # replace old item with new object, id has been kept the same
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_random_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(first_name="Name to be updated", last_name="Name to be updated"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Alexey")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    contact.last_name = old_contacts[index].last_name
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
