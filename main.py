# -*- coding: utf-8 -*-
# @Filename : main
# @Date : 2022-07-25-15-27
# @Project: nt-integration-sdk

from notion_py.page import Page
from notion_py.database import Database


if __name__ == '__main__':
    db = Database()
    _builder = db.new_builder()
    _builder.edit_title(plain_text="[DB]New Text")
    db.update(database_id="476a04a6be064fc1b3efd15b68e15e79", builder=_builder)
