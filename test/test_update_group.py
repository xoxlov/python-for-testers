# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_update_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    # create new Group object with data for update
    group = Group(name="UpdatedGroup", header="UpdatedGroupHeader", footer="UpdatedGroupFooter")
    # set object id to the group id by index
    group.id = old_groups[index].id
    app.group.update_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    # change group by index to the new object, id has been kept
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_update_all_empty_groups(app):
    old_groups = app.group.get_group_list()
    app.group.update_all_empty_groups(Group(name="UpdatedFromEmptyGroup",
                                            header="UpdatedFromEmptyGroupHeader",
                                            footer="UpdatedFromEmptyGroupFooter"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
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


def test_update_random_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Updated Group Name")
    group.id = old_groups[index].id
    app.group.update_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    group.header = old_groups[index].header
    group.footer = old_groups[index].footer
    group.id = old_groups[index].id
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_update_random_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="Updated Group Header")
    app.group.update_group_by_index(Group(header="Updated Group Header"), index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    group.name = old_groups[index].name
    group.footer = old_groups[index].footer
    group.id = old_groups[index].id
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
