class ContactHelper():
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        contact_data = {
            "firstname": contact.first_name,
            "lastname": contact.last_name,
            "work": contact.work_phone,
            "title": contact.position,
            "company": contact.company,
            "address": contact.address_1,
            "email": contact.email
        }
        for key in contact_data:
            self._fill_input_data_field(key, contact_data[key])
        wd.find_element_by_name("submit").click()
        self.app.open_homepage_by_link()

    def _fill_input_data_field(self, field_name, value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)

