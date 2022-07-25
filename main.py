# -*- coding: utf-8 -*-
# @Filename : main
# @Date : 2022-07-25-15-27
# @Project: nt-integration-sdk



from notion_integration_py.database import Database


if __name__ == '__main__':
    d = Database("Name", "test", "476a04a6be064fc1b3efd15b68e15e79")
    d.add_rich_text(key="Description", plain_text="xxxxx", annotations={"bold": True})
    print(d.export2json())
