# -*- coding: utf-8 -*-
# @Filename : __init__.py
# @Date : 2022-07-25-10-33
# @Project: nt-integration-sdk

from abc import ABC, abstractmethod
from enum import Enum
from notion_integration_py.utils import utils


class NotionObject(ABC):
    @staticmethod
    def loads(**data):
        """Deserialize to python object

        Returns:

        """
        pass

    def export2json(self):
        """Export Object as Json Format

        Returns:

        """
        return utils.obj2dict(self)

    def _auto_update_attributes(self, **kwargs):
        """Create all attributes that exist on variable `xargs` on current object

        Args:
            **xargs: args object

        """
        for key in kwargs.keys():
            self._update_attribute(key, kwargs[key])

    def _update_attribute(self, name, value):
        """Create an attribute on current object

        Args:
            name (string): attribute name
            value (any): attribute value

        """
        if value is not None:
            if isinstance(value, Enum):
                value = value.value
            setattr(self, name, value)

    def __getattr__(self, item):
        """
        Is an object method that is called if the object’s properties are not found.
        """
        return ""
