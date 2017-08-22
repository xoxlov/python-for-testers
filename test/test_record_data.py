from model.contact import Contact

def test_record_data_on_home_page(app, db):
    contacts_from_ui = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert len(contacts_from_ui) == len(contacts_from_db)
    assert sorted(contacts_from_ui, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)

def test_record_data_on_view_page(app):
    for index in range(app.contact.count()):
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
        assert contact_from_view_page.full_name == contact_from_edit_page.get_full_name()
        assert contact_from_view_page.all_phones == contact_from_edit_page.all_phones
        assert contact_from_view_page.all_emails == contact_from_edit_page.all_emails
