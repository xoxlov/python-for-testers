# -*- coding: utf-8 -*-
from sys import maxsize

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
        separator = ' '
        # in case of any missing name - don't print space between first name and last name
        if self.last_name is None or self.last_name == '' or self.first_name is None or self.first_name == '':
            separator = ''
        return "{a}: '{b}{s}{c}'".format(a=self.id, b=self.first_name, c=self.last_name, s=separator)

    def __eq__(self, other):
        # for equality check field separately: id, last and first names
        id_equal = self.id is None or other.id is None or self.id == other.id
        fname_equal = (self.first_name == other.first_name) or (self.first_name == None and other.first_name == '')
        lname_equal = (self.last_name == other.last_name) or (self.last_name == None and other.last_name == '')
        return id_equal and fname_equal and lname_equal

    def id_or_max(self):
        return int(self.id) if self.id else maxsize
