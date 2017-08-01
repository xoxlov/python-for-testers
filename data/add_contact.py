# -*- coding: utf-8 -*-
import random
import string
from model.contact import Contact


CONTACTS = [
    Contact(first_name="name1", last_name="lastname1", work_phone="+71111111111", home_phone="+71111112222"),
    Contact(first_name="name2", last_name="lastname2", work_phone="+72222221111", home_phone="+72222222222")
]


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


NUMBER_OF_CASES = 1
testdata = [Contact()] + \
           [Contact(first_name=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="bd_year", bd_year=random.randint(0, 10000)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="bd_year", bd_year=random_string("", 5)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="middlename", middle_name=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="lastname", last_name=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="nickname", nickname=random_string("", 10)) for i in range(NUMBER_OF_CASES)]  + \
           [Contact(first_name="address", address=random_string("", 50)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="work_phone", work_phone=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="mobile_phone", mobile_phone=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="home_phone", home_phone=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="fax", fax=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="title", title=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="company", company=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="homepage", homepage=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="homepage", homepage=random_url(10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="SecAddr", secondary_address=random_string("", 50)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="SecPhone", secondary_phone=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="notes", notes=random_string("", 50)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="email", email=random_string("email", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="email2", email2=random_string("email2", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="email3", email3=random_string("email3", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="email", email=random_email("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="email2", email2=random_email("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="email3", email3=random_email("", 10)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="anniv_year", anniv_year=random.randint(0, 10000)) for i in range(NUMBER_OF_CASES)] + \
           [Contact(first_name="anniv_year", anniv_year=random_string("", 5)) for i in range(NUMBER_OF_CASES)]
           # commented are fields that are not implemented as input data due to they require special processing
           # bd_day, anniv_day
           # bd_month, anniv_month

