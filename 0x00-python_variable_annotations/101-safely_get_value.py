#!/usr/bin/env python3
"""Function with type annotations"""
from typing import Mapping, Any, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[None, TypeVar('T')]) -> Union[
                                                            Any,
                                                            TypeVar('T')]:
    """Returns key in a dictionary or default"""
    if key in dct:
        return dct[key]
    else:
        return default


annotations = safely_get_value.__annotations__


print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))
