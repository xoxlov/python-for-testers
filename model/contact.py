# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, first_name=None, last_name=None, work_phone=None,
                 position=None, company=None, address_1=None,
                 email=None):
        self.first_name = first_name or ""
        self.last_name = last_name or ""
        self.work_phone = work_phone or ""
        self.position = position or ""
        self.company = company or ""
        self.address_1 = address_1 or ""
        self.email = email or ""
