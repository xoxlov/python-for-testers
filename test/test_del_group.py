# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be deleted"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    # group[index] in old list was removed
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be deleted"))
    app.group.delete_all_groups()
    new_groups = app.group.get_group_list()
    # need to check the length of new list to be 0, i.e. list is empty
    assert len(new_groups) == 0
