# -*- coding: utf-8 -*-
import os.path
import random
import string
import json
import sys
import getopt
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


try:
    opts, agrs = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as e:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for op, arg in opts:
    if op == "-n":
        n = int(arg)
    elif op == "-f":
        f = arg

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("Name", 10), header=random_string("Header", 20), footer=random_string("Footer", 20))
    for count in range(n)
]

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file_name, "w") as file:
    file.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
file.close()
