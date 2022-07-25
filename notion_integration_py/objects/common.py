# -*- coding: utf-8 -*-
# @Filename : common
# @Date : 2022-07-25-10-36
# @Project: nt-integration-sdk

from enum import Enum
from . import NotionObject


class RichTextType(Enum):
    text = "text"
    mention = "mention"
    equation = "equation"


class Color(Enum):
    default = "default"
    gray = "gray"
    brown = "brown"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    purple = "purple"
    pink = "pink"
    red = "red"
    gray_background = "gray_background"
    brown_background = "brown_background"
    orange_background = "orange_background"
    yellow_background = "yellow_background"
    green_background = "green_background"
    blue_background = "blue_background"
    purple_background = "purple_background"
    pink_background = "pink_background"
    red_background = "red_background"


class SelectColor(Enum):
    default = "default"
    gray = "gray"
    brown = "brown"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    purple = "purple"
    pink = "pink"
    red = "red"


class ParentType(Enum):
    database_id = "database_id"
    page_id = "page_id"


class RichText(NotionObject):
    def __init__(self,
                 plain_text: str,
                 href: str = None,
                 annotations: dict = None,
                 type: str = None, **kwargsa):
        self._auto_update_attributes(plain_text=plain_text,
                                     href=href,
                                     annotations=Annotations(**annotations) if annotations else None,
                                     type=getattr(RichTextType, str(type), None))


class Annotations(NotionObject):
    def __init__(self,
                 bold: bool = None,
                 italic: bool = None,
                 strikethrough: bool = None,
                 underline: bool = None,
                 code: bool = None,
                 color: str = None,
                 **kwargsa):
        self._auto_update_attributes(
            bold=bold,
            italic=italic,
            strikethrough=strikethrough,
            underline=underline,
            code=code,
            color=getattr(Color, str(color), None)
        )


class Text(NotionObject):
    def __init__(self, content: str, link: str = None, **kwargs):
        self._auto_update_attributes(content=content,
                                     link=Link(url=link) if link else None)


class Link(NotionObject):
    def __init__(self, url: str, **kwargs):
        self._auto_update_attributes(type="url", url=url)


class Select(NotionObject):
    def __init__(self, name: str, color: str = None, **kwargs):
        self._auto_update_attributes(name=name, color=getattr(SelectColor, str(color), None))


class Date(NotionObject):
    def __init__(self, start: str, end: str = None, time_zone: str = None, **kwargs):
        self._auto_update_attributes(start=start, end=end, time_zone=time_zone)


class People(NotionObject):
    def __init__(self, user_id: str, **kwargs):
        self._auto_update_attributes(object="user", id=user_id)


class File(NotionObject):
    def __init__(self, name: str, url: str):
        self._auto_update_attributes(type="external",
                                     name=name,
                                     external={"url": url})


class Formula(NotionObject):
    def __init__(self, expression: str):
        self._auto_update_attributes(expression=expression)


class Parent(NotionObject):
    def __init__(self, parent_id: str, parent_type="database_id"):
        if parent_type is None:
            parent_type = "database_id"
        _parent_type = getattr(ParentType, parent_type).value
        self._update_attribute("type", _parent_type)
        self._update_attribute(_parent_type, parent_id)
