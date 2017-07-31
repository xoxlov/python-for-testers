# -*- coding: utf-8 -*-
from sys import maxsize

class Contact:

    def __init__(self, id=None,
                 first_name=None, middle_name=None, last_name=None, nickname=None,
                 company=None, title=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 bd_day=None, bd_month=None, bd_year=None,
                 anniv_day=None, anniv_month=None, anniv_year=None,
                 secondary_address=None, secondary_phone=None,
                 notes=None, full_name=None, all_phones=None, all_emails=None
                 ):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname

        self.company = company
        self.title = title
        self.address = address

        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax

        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage

        self.bd_day = bd_day
        self.bd_month = bd_month
        self.bd_year = bd_year
        self.anniv_day = anniv_day
        self.anniv_month = anniv_month
        self.anniv_year = anniv_year

        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.notes = notes

        self.full_name = full_name
        self.all_phones = all_phones
        self.all_emails = all_emails

    def get_full_name(self):
        self.full_name = ' '.join(map(lambda x: x.strip(),
                                      filter(lambda x: x is not None,
                                             [self.first_name, self.middle_name, self.last_name]))).rstrip()
        return self.full_name

    def get_short_full_name(self):
        return ' '.join(map(lambda x: x.strip(),
                            filter(lambda x: x is not None,
                                   [self.first_name, self.last_name]))).rstrip()

    def __repr__(self):
        return "%s: %s" % (self.id, self.get_full_name())

    def __str__(self):
        output = "%s: %s" % (self.id, self.first_name)
        for d in self.__dict__:
            if self.__getattribute__(d) and d not in ["id", "first_name"]:
                output += "; %s: %s" % (d, self.__getattribute__(d))
        return output

    def __eq__(self, other):
        id_equal = self.id is None or other.id is None or self.id == other.id
        return id_equal and self.get_short_full_name() == other.get_short_full_name()

    def id_or_max(self):
        return int(self.id) if self.id else maxsize
