# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, first_name=None, last_name=None, work_phone=None,
                 position=None, company=None, address_1=None,
                 email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.work_phone = work_phone
        self.position = position
        self.company = company
        self.address_1 = address_1
        self.email = email
        self.id = id

    def __repr__(self):
        return "Contact(name='{a} {b}'; id={c})".format(a=self.first_name, b=self.last_name, c=self.id)