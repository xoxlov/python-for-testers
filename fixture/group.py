# -*- coding: utf-8 -*-
from model.group import Group


class GroupHelper():
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and wd.find_elements_by_name("new"):
            return
        wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self._fill_group_data(group)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def _select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self._select_first_group()
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        # find and select all groups on page
        groups_list = wd.find_elements_by_name("selected[]")
        for index in range(len(groups_list)):
            groups_list[index].click()
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def update_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self._select_first_group()
        wd.find_element_by_name("edit").click()
        self._fill_group_data(group)
        wd.find_element_by_name("update").click()
        self.open_groups_page()

    def update_all_empty_groups(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # try to find the full list of contacts records
        groups_list = wd.find_elements_by_css_selector("span.group")
        # if any records found then analyze them
        index = 0
        while index < len(groups_list):
            # get group name and check if it isn't empty - then continue without update
            groupname = groups_list[index].get_property("textContent")
            if groupname:
                index += 1
                continue
            # group with no name found
            groups_list[index].click()
            wd.find_element_by_name("edit").click()
            self._fill_group_data(group)
            wd.find_element_by_name("update").click()
            self.open_groups_page()
            groups_list = wd.find_elements_by_css_selector("span.group")
            # reset index counter due to list of contacts has changed and we need to analyze from scratch
            index = 0
        self.open_groups_page()

    def _fill_group_data(self, group):
        group_data = {"group_name": group.name,
                      "group_header": group.header,
                      "group_footer": group.footer}
        for key in group_data:
            self._type_input_value(key, group_data[key])

    def _type_input_value(self, location, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(location).click()
            wd.find_element_by_name(location).clear()
            wd.find_element_by_name(location).send_keys(value)

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups_list = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups_list.append(Group(name=text, id=id))
        return groups_list