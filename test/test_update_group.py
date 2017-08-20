# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_update_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group to be updated"))
    old_groups = db.get_group_list()
    group_to_update = random.choice(old_groups)
    group = Group(id=group_to_update.id, name="UpdatedGroup", header="UpdatedGroupHeader", footer="UpdatedGroupFooter")
    app.group.update_group_by_id(group, group_to_update.id)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_to_update)] = group
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


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
