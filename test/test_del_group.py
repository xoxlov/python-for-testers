# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be deleted"))
    app.group.delete_first_group()


def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be deleted"))
    app.group.delete_all_groups()
