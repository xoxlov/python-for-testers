# -*- coding: utf-8 -*-
import os.path
import random
import string
import jsonpickle
import sys
import getopt
from model.contact import Contact


def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_url(maxlen):
    symbols = string.ascii_letters + string.digits
    upper_domain = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    lower_domain = "".join([random.choice(symbols) for i in range(3)])
    return "http://" + upper_domain + lower_domain


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    email_name = random_string("", 10)
    upper_domain = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    lower_domain = "".join([random.choice(symbols) for i in range(3)])
    return random_string(prefix, 10) + email_name + "@" + upper_domain + "." + lower_domain


try:
    opts, agrs = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as e:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for op, arg in opts:
    if op == "-n":
        n = int(arg)
    elif op == "-f":
        f = arg

testdata = [Contact()] + \
           [Contact(first_name=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="bd_year", bd_year=random.randint(0, 10000)) for i in range(n)] + \
           [Contact(first_name="bd_year", bd_year=random_string("", 5)) for i in range(n)] + \
           [Contact(first_name="middlename", middle_name=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="lastname", last_name=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="nickname", nickname=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="address", address=random_string("", 50)) for i in range(n)] + \
           [Contact(first_name="work_phone", work_phone=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="mobile_phone", mobile_phone=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="home_phone", home_phone=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="fax", fax=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="title", title=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="company", company=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="homepage", homepage=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="homepage", homepage=random_url(10)) for i in range(n)] + \
           [Contact(first_name="SecAddr", secondary_address=random_string("", 50)) for i in range(n)] + \
           [Contact(first_name="SecPhone", secondary_phone=random_string("", 10)) for i in range(n)] + \
           [Contact(first_name="notes", notes=random_string("", 50)) for i in range(n)] + \
           [Contact(first_name="email", email=random_string("email", 10)) for i in range(n)] + \
           [Contact(first_name="email2", email2=random_string("email2", 10)) for i in range(n)] + \
           [Contact(first_name="email3", email3=random_string("email3", 10)) for i in range(n)] + \
           [Contact(first_name="email", email=random_email("", 10)) for i in range(n)] + \
           [Contact(first_name="email2", email2=random_email("", 10)) for i in range(n)] + \
           [Contact(first_name="email3", email3=random_email("", 10)) for i in range(n)] + \
           [Contact(first_name="anniv_year", anniv_year=random.randint(0, 10000)) for i in range(n)] + \
           [Contact(first_name="anniv_year", anniv_year=random_string("", 5)) for i in range(n)]
           # commented are fields that are not implemented as input data due to they require special processing
           # bd_day, anniv_day
           # bd_month, anniv_month

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file_name, "w") as file:
    jsonpickle.set_encoder_options("json", indent=2)
    file.write(jsonpickle.encode(testdata))
file.close()
