# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.add_new(Contact(first_name="Maxim", last_name="Pichugin",
                                work_phone="+7.111.111.1111",
                                position="Main Boss", company="Cherehapa Ltd.",
                                address_1="Moscow", email="email@mail.me"))


def test_add_new_empty_contact(app):
    app.contact.add_new(Contact())
