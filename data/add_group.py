# -*- coding: utf-8 -*-
import random
import string
from model.group import Group


GROUPS = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("Name", 10), header=random_string("Header", 20), footer=random_string("Footer", 20))
    for count in range(5)
]
