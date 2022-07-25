# -*- coding: utf-8 -*-
# @Filename : main
# @Date : 2022-07-25-15-27
# @Project: nt-integration-sdk


from notion_integration_py.objects.properties import DateProperty
from notion_integration_py.utils.utils import iso8601_date



if __name__ == '__main__':
    x = DateProperty(start=iso8601_date(year="2022", month="01"), end=iso8601_date(year="2022", month="02"))
    print(x.export2json())
