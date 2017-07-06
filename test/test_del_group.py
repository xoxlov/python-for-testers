# -*- coding: utf-8 -*-


def test_delete_first_group(app):
    app.group.delete_first_group()


def test_delete_all_groups(app):
    app.group.delete_all_groups()
