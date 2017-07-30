# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

groups_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("Name", 10), header=random_string("Header", 20), footer=random_string("Footer", 20))
    for count in range(5)
]


@pytest.mark.parametrize("group", groups_data, ids=[repr(x) for x in groups_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # new list is made of old list with new item added
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
