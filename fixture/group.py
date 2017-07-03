# -*- coding: utf-8 -*-


class GroupHelper():
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self._fill_input_data_field("group_name", group.name)
        self._fill_input_data_field("group_header", group.header)
        self._fill_input_data_field("group_footer", group.footer)
        wd.find_element_by_name("submit").click()
        # return to the groups page
        self.open_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group on page if any
        groups_list = wd.find_elements_by_name("selected[]")
        if (len(groups_list)):
            groups_list[0].click()
            # submit deletion
            wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        # find and select all groups on page
        groups_list = wd.find_elements_by_name("selected[]")
        if (len(groups_list)):
            for index in range(len(groups_list)):
                groups_list[index].click()
            # submit deletion
            wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def _fill_input_data_field(self, field_name, value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)
