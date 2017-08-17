# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group to be deleted"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group to be deleted"))
    app.group.delete_all_groups()
    new_groups = app.group.get_group_list()
    # need to check the length of new list to be 0, i.e. list is empty
    assert len(new_groups) == 0
