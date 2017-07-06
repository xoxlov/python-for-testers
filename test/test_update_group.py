# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    app.group.update_first_group(Group(name="UpdatedGroup",
                                       header="UpdatedGroupHeader",
                                       footer="UpdatedGroupFooter"))


def test_update_all_empty_groups(app):
    app.group.update_all_empty_groups(Group(name="UpdatedFromEmptyGroup",
                                            header="UpdatedFromEmptyGroupHeader",
                                            footer="UpdatedFromEmptyGroupFooter"))


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    app.group.update_first_group(Group(name="Updated Group Name"))


def test_update_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    app.group.update_first_group(Group(header="Updated Group Header"))
