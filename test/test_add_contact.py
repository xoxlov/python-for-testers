# -*- coding: utf-8 -*-
import pytest
import string
import random
from model.contact import Contact


NUMBER_OF_CASES = 3


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix):
    random_string(prefix,10) + "@" + random_string("", 10) + "." + random_string("", 4)


contact_data = [Contact()] + \
               [Contact(first_name=random_string("", 10)) for i in range(NUMBER_OF_CASES)] + \
               [Contact(first_name="middlename", middle_name=random_string("MName", 10)) for i in range(NUMBER_OF_CASES)] + \
               [Contact(first_name="lastname", last_name=random_string("LName", 10)) for i in range(NUMBER_OF_CASES)] + \
               [Contact(first_name="nickname", nickname=random_string("aka", 10)) for i in range(NUMBER_OF_CASES)]  + \
               [Contact(first_name="address", address=random_string("address", 50)) for i in range(NUMBER_OF_CASES)]

               # комментированные строки - всего лишь демонстрация, как оно могло бы выглядеть, если бы надо было
               # делать проверки для всех полей, реализация добавит ненужной работы, так что пока без неё....
               # В дальнейшем эти варианты все будут удалены.
               # [Contact(first_name="work_phone", work_phone=random_string("WP", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="mobile_phone", mobile_phone=random_string("MP", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="home_phone", home_phone=random_string("HP", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="fax", fax=random_string("fax", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="title", title=random_string("title", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="company", company=random_string("company", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="email", email=random_string("email", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="email2", email2=random_string("email2", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="email3", email3=random_string("email3", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="homepage", homepage=random_string("http://", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="bd_day", bd_day=random.randint(0, 31)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="anniv_day", anniv_day=random.randint(0, 31)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="bd_year", bd_year=random.randint(0, 10000)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="anniv_year", anniv_year=random.randint(0, 10000)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="SecAddr", secondary_address=random_string("SecAddr ", 50)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="SecPhone", secondary_phone=random_string("SP", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="notes", notes=random_string("Notes: ", 50)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="address", address=random_string("address", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="address", address=random_string("address", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="address", address=random_string("address", 10)) for i in range(NUMBER_OF_CASES)] + \
               # [Contact(first_name="address", address=random_string("address", 10)) for i in range(NUMBER_OF_CASES)]
               # #bd_month = None, anniv_month = None

@pytest.mark.parametrize("contact", contact_data, ids=[repr(x) for x in contact_data])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    print(sorted(old_contacts, key=Contact.id_or_max))
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
