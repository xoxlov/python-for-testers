
def test_record_data_on_home_page(app):
    for index in range(app.contact.count()):
        contact_from_contact_page = app.contact.get_contact_from_contact_list(index)
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
        assert contact_from_contact_page.get_full_name() == contact_from_edit_page.get_short_full_name()
        assert contact_from_contact_page.address == contact_from_edit_page.address
        assert contact_from_contact_page.all_phones == contact_from_edit_page.all_phones
        assert contact_from_contact_page.all_emails == contact_from_edit_page.all_emails

def test_record_data_on_view_page(app):
    for index in range(app.contact.count()):
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
        assert contact_from_view_page.full_name == contact_from_edit_page.get_full_name()
        assert contact_from_view_page.all_phones == contact_from_edit_page.all_phones
        assert contact_from_view_page.all_emails == contact_from_edit_page.all_emails
