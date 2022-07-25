# -*- coding: utf-8 -*-
# @Filename : utils
# @Date : 2022-07-25-13-30
# @Project: nt-integration-sdk

import datetime


def obj2dict(obj):
    if not hasattr(obj, "__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        # avoiding exposure to the protect&private attribute
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(obj2dict(item))
        else:
            element = obj2dict(val)
        result[key] = element
    return result


def iso8601_date(year=2022, month=1, day=1, hours=00, minutes=00, seconds=00, include_time: bool = False):
    dt = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes), int(seconds), 000000)
    if include_time:
        formatter = "%Y-%m-%dT%H:%M:%SZ"
    else:
        formatter = "%Y-%m-%d"

    return dt.strftime(formatter)
