# -*- coding: utf-8 -*-


class GroupHelper():
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self._fill_input_data(group)
        wd.find_element_by_name("submit").click()
        # return to the groups page
        self.app.open_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.open_groups_page()
        # select first group on page if any
        groups_list = wd.find_elements_by_name("selected[]")
        if (len(groups_list)):
            groups_list[0].click()
            # submit deletion
            wd.find_element_by_name("delete").click()
        self.app.open_groups_page()

    def delete_all_groups(self):
        wd = self.app.wd
        self.app.open_groups_page()
        # find and select all groups on page
        groups_list = wd.find_elements_by_name("selected[]")
        if (len(groups_list)):
            for index in range(len(groups_list)):
                groups_list[index].click()
            # submit deletion
            wd.find_element_by_name("delete").click()
        self.app.open_groups_page()

    def update_first_group(self, group):
        wd = self.app.wd
        self.app.open_groups_page()
        groups_list = wd.find_elements_by_name("selected[]")
        if groups_list:
            groups_list[0].click()
            wd.find_element_by_name("edit").click()
            self._fill_input_data(group)
            wd.find_element_by_name("update").click()
            self.app.open_groups_page()

    def update_all_empty_groups(self, group):
        wd = self.app.wd
        self.app.open_groups_page()
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
            self._fill_input_data(group)
            wd.find_element_by_name("update").click()
            self.app.open_groups_page()
            groups_list = wd.find_elements_by_css_selector("span.group")
            # reset index counter due to list of contacts has changed and we need to analyze from scratch
            index = 0
        self.app.open_groups_page()

    def _fill_input_data(self, group):
        wd = self.app.wd
        group_data = {
            "group_name": group.name,
            "group_header": group.header,
            "group_footer": group.footer
        }
        for key in group_data:
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(group_data[key])

