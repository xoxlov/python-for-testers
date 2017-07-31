# -*- coding: utf-8 -*-
import pytest
import string
import random
from model.contact import Contact


NUMBER_OF_CASES = 1


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


contact_data = [Contact()] + \
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

@pytest.mark.parametrize("contact", contact_data, ids=[str(x) for x in contact_data])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
