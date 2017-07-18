# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = app.group.get_group_list()
    # create new Group object with data for update
    group = Group(name="UpdatedGroup", header="UpdatedGroupHeader", footer="UpdatedGroupFooter")
    # set object id to the first listed group id
    group.id = old_groups[0].id
    app.group.update_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    # change first listed group to the new object, id has been kept
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_update_all_empty_groups(app):
    old_groups = app.group.get_group_list()
    app.group.update_all_empty_groups(Group(name="UpdatedFromEmptyGroup",
                                            header="UpdatedFromEmptyGroupHeader",
                                            footer="UpdatedFromEmptyGroupFooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    # go through the groups list and look for empty groups
    for i in range(len(old_groups)):
        if old_groups[i].name == '':
            # if the empty group found - create new Group object with data for update
            # object should be new every time to escape redefinition with shared pointer
            group = Group(name="UpdatedFromEmptyGroup", header="UpdatedFromEmptyGroupHeader", footer="UpdatedFromEmptyGroupFooter")
            # set id for updated group
            group.id = old_groups[i].id
            # replace old item with new object, id has been kept the same
            old_groups[i] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = app.group.get_group_list()
    group = Group(name="Updated Group Name")
    group.id = old_groups[0].id
    app.group.update_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.header = old_groups[0].header
    group.footer = old_groups[0].footer
    group.id = old_groups[0].id
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_update_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = app.group.get_group_list()
    group = Group(header="Updated Group Header")
    app.group.update_first_group(Group(header="Updated Group Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.name = old_groups[0].name
    group.footer = old_groups[0].footer
    group.id = old_groups[0].id
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
