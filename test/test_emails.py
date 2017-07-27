# This module is legacy due to all required asserts are included in test_record_data.py
# refer to functions test_record_data_on_home_page() and test_record_data_on_view_page()

def test_emails_on_home_page(app):
    for index in range(app.contact.count()):
        contact_from_contact_page = app.contact.get_contact_from_contact_list(index)
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
        assert contact_from_contact_page.all_emails == contact_from_edit_page.all_emails


def test_emails_on_contact_view_page(app):
    for index in range(app.contact.count()):
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
        assert contact_from_view_page.all_emails == contact_from_edit_page.all_emails
