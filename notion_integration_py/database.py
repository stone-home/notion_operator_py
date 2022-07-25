# -*- coding: utf-8 -*-
# @Filename : database
# @Date : 2022-07-25-17-51
# @Project: nt-integration-sdk


from .objects import NotionObject
from .objects.common import Parent
from .objects.properties import (
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
    PropertyObject
)


class DatabaseObject(NotionObject):
    pass


class Properties(DatabaseObject):
    def __init__(self, key: str, title: str):
        self._update_attribute(key, TitleProperty(title))

    def edit_property(self, key, value: PropertyObject):
        if isinstance(value, PropertyObject) is False:
            raise TypeError(f"Property Object Type Error, {type(value)}")
        self._update_attribute(key, value)

    def get_property(self, key):
        return getattr(self, key)


class Database(DatabaseObject):
    def __init__(self, title_key: str, title: str, parent_id: str, parent_type="database_id"):
        self.edit_parent(parent_id, parent_type)
        self.properties = Properties(key=title_key, title=title)

    def edit_parent(self, parent_id, parent_type='database_id'):
        setattr(self, "parent", Parent(parent_id=parent_id, parent_type=parent_type))

    def add_rich_text(self, key: str, plain_text: str, annotations: dict = None):
        self.properties.edit_property(key, RichTextProperty(plain_text, annotations=annotations))

    def add_number(self, key: str, number: int):
        self.properties.edit_property(key, NumberProperty(number))

    def add_select(self, key: str, select_name: str, select_color: str = None):
        self.properties.edit_property(key, SelectProperty(select_name, select_color))





