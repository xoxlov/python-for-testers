# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="UpdatedGroup",
                                       header="UpdatedGroupHeader",
                                       footer="UpdatedGroupFooter"))
    app.session.logout()


def test_update_all_empty_groups(app):
    app.session.login(username="admin", password="secret")
    app.group.update_all_empty_groups(Group(name="UpdatedFromEmptyGroup",
                                            header="UpdatedFromEmptyGroupHeader",
                                            footer="UpdatedFromEmptyGroupFooter"))
    app.session.logout()
