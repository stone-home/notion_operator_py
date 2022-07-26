# -*- coding: utf-8 -*-
# @Filename : database
# @Date : 2022-07-25-17-51
# @Project: nt-integration-sdk


from .objects import (
    NotionObject,
    Parent,
    TitleProperty,
    RichTextProperty,
    NumberProperty,
    SelectProperty,
    MultipleSelectProperty,
    DateProperty,
    PeopleProperty,
    FileProperty,
    CheckBoxProperty,
    URLProperty,
    EmailProperty,
    PhoneNumberProperty,
    FormulaProperty,
    Properties
)


class PageObject(NotionObject):
    pass


class Page(PageObject):
    def __init__(self, title_key: str, title: str, parent_id: str, parent_type="database_id"):
        self.edit_parent(parent_id, parent_type)
        self.properties = Properties(key=title_key, title=title)

    def edit_parent(self, parent_id, parent_type='database_id'):
        setattr(self, "parent", Parent(parent_id=parent_id, parent_type=parent_type))

    def add_rich_text(self, key: str, plain_text: str, annotations: dict = None):
        return self.properties.update_property(key, RichTextProperty(plain_text, annotations=annotations))

    def add_number(self, key: str, number: int):
        return self.properties.update_property(key, NumberProperty(number))

    def add_select(self, key: str, select_name: str, select_color: str = None):
        return self.properties.update_property(key, SelectProperty(select_name, select_color))

    def add_date(self, key: str, start: str, end: str = None, time_zone: str = None):
        return self.properties.update_property(key, DateProperty(start, end, time_zone))

    def add_checkbox(self, key: str, checked: bool = False):
        return self.properties.update_property(key, CheckBoxProperty(checked))

    def add_url(self, key: str, url: str):
        return self.properties.update_property(key, URLProperty(url))

    def add_email(self, key: str, email: str):
        return self.properties.update_property(key, EmailProperty(email))

    def add_phone_number(self, key: str, phone_number: str):
        return self.properties.update_property(key, PhoneNumberProperty(phone_number))

    def add_formula(self, key: str, experssion: str):
        return self.properties.update_property(key, FormulaProperty(experssion))

    def add_multiple_select(self, key: str):
        return self.properties.update_property(key, MultipleSelectProperty())

    def add_people(self, key: str):
        return self.properties.update_property(key, PeopleProperty())

    def add_file(self, key: str):
        return self.properties.update_property(key, FileProperty())

    def remove_property(self, key):
        self.properties.delete_property(key)






