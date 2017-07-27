# -*- coding: utf-8 -*-
from model.contact import Contact


contact_list = [Contact(first_name="Maxim", last_name="Pichugin",
                        work_phone="+7.111.111.1111",
                        title="Main Boss", company="Cherehapa Ltd.",
                        address="Moscow", email="email@mail.me"),
                Contact()]

def test_add_new_contact(app):
    for contact in contact_list:
        old_contacts = app.contact.get_contact_list()
        app.contact.add_new(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
