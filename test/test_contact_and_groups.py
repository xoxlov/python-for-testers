from model.group import Group
import random


def test_add_random_contact_in_random_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_test_user("Contact for Group Update")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group for contact"))
    all_contacts = db.get_contact_list()
    all_groups = db.get_group_list()
    contact = random.choice(all_contacts)
    group = random.choice(all_groups)
    if contact in db.get_contacts_in_group(group):
        return
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in db.get_contacts_in_group(group)
    assert contact not in db.get_contacts_not_in_group(group)


def test_delete_contact_from_group(app, db):
    # select only groups with contacts
    all_groups = list(gr for gr in db.get_group_list() if len(db.get_contacts_in_group(group=gr)))
    if not all_groups: # no groups - do nothing and return
        return
    group = random.choice(all_groups)
    all_contacts = db.get_contacts_in_group(group=group)
    contact = random.choice(all_contacts)
    app.contact.delete_contact_from_group(contact.id, group.id)
    assert contact not in db.get_contacts_in_group(group)
    assert contact in db.get_contacts_not_in_group(group)
