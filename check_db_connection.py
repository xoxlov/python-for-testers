# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    result_list = db.get_contacts_in_group(Group(id="11"))
    # result_list = db.get_contact_list()
    for item in result_list:
        print(item)
    print(len(result_list))
finally:
    db.destroy()
