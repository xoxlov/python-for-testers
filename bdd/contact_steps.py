from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <middlename> , <lastname>, <address>, <email>, <homephone> and <mobilephone>')
def new_contact(firstname, middlename, lastname, address, email, homephone, mobilephone):
    return Contact(first_name=firstname, middle_name=middlename, last_name=lastname,
                   address=address, email=email, home_phone=homephone, mobile_phone=mobilephone)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.add_new(new_contact)

@then('the new contact list is equal to the old list with added contact')
def verify_added_contact(db, contact_list, new_contact):
    old_contact_list = contact_list
    new_contact_list = db.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="Contact to be deleted", lastname="Contact to be deleted"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list without deleted contact')
def verify_deleted_contact(db, non_empty_contact_list, random_contact):
    old_contact_list = non_empty_contact_list
    old_contact_list.remove(random_contact)
    new_contact_list = db.get_contact_list()
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


@given('a contact with <firstname>, <lastname>, <address>, <email> and <homephone>')
def updated_contact(firstname, lastname, address, email, homephone):
    return Contact(first_name=firstname, last_name=lastname, address=address, email=email, home_phone=homephone)

@when('I update the random contact from the list with the new contact data')
def modify_contact(app, random_contact, updated_contact):
    app.contact.update_contact_by_id(updated_contact, random_contact.id)

@then('the modified contact list is equal to the old list with updated contact data')
def verify_updated_contact(db, non_empty_contact_list, random_contact, updated_contact):
    old_contact_list = non_empty_contact_list
    updated_contact.id = random_contact.id
    old_contact_list[old_contact_list.index(random_contact)] = updated_contact
    new_contact_list = db.get_contact_list()
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
