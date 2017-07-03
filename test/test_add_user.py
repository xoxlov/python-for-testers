# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact(Contact(first_name="Maxim", last_name="Pichugin",
                                work_phone="+7.111.111.1111",
                                position="Main Boss", company="Cherehapa Ltd.",
                                address_1="Moscow", email="email@mail.me"))
    app.session.logout()


def test_add_new_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact(Contact())
    app.session.logout()
