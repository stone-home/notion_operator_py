# -*- coding: utf-8 -*-
# @Filename : database_properties
# @Date : 2022-07-25-14-50
# @Project: nt-integration-sdk

from . import NotionObject
from .common import Text, RichText, Select, Date, People, File, Formula, Annotations


class PropertyObject(NotionObject):
    pass


class _Text(PropertyObject):
    def __init__(self, content: str):
        self._auto_update_attributes(text=Text(content=content))


class TitleProperty(PropertyObject):
    def __init__(self, content: str):
        self._auto_update_attributes(title=[_Text(content)])


class _RichText(PropertyObject):
    def __init__(self, content: str, annotations: dict = None):
        self._auto_update_attributes(text=Text(content=content),
                                     annotations=Annotations(**annotations) if annotations else None)


class RichTextProperty(PropertyObject):
    def __init__(self, content: str, annotations: dict = None):
        self._auto_update_attributes(rich_text=[_RichText(content, annotations)])


class NumberProperty(PropertyObject):
    def __init__(self, number: int):
        self._auto_update_attributes(number=number)


class SelectProperty(PropertyObject):
    def __init__(self, name: str, color: str = None):
        self._auto_update_attributes(select=Select(name=name, color=color))


class MultipleSelectProperty(PropertyObject):
    def __init__(self):
        self._auto_update_attributes(multi_select=[])

    def add_select(self, name: str, color: str = None):
        self.multi_select.append(Select(name=name, color=color))


class DateProperty(PropertyObject):
    def __init__(self, start: str, end: str = None, time_zone: str = None):
        self._auto_update_attributes(date=Date(start, end, time_zone))


class PeopleProperty(PropertyObject):
    def __init__(self):
        self._auto_update_attributes(people=[])

    def add_people(self, user_id):
        self.people.append(People(user_id=user_id))


class FileProperty(PropertyObject):
    def __init__(self):
        self._auto_update_attributes(files=[])

    def add_file(self, name: str, url: str):
        self.files.append(File(name, url))


class CheckBoxProperty(PropertyObject):
    def __init__(self, checked: bool = False):
        self._auto_update_attributes(checkbox=checked)


class URLProperty(PropertyObject):
    def __init__(self, url: str):
        self._auto_update_attributes(url=url)


class EmailProperty(PropertyObject):
    def __init__(self, email: str):
        self._auto_update_attributes(email=email)


class PhoneNumberProperty(PropertyObject):
    def __init__(self, phone_number: str):
        self._auto_update_attributes(phone_number=phone_number)


class FormulaProperty(PropertyObject):
    def __init__(self, experssion: str):
        self._auto_update_attributes(formula=Formula(experssion))


# todo: notion have not implemented those two API
# class RelationProperty(NotionObject):
# class RolloutProperty(NotionObject):
