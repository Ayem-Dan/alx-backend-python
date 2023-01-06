#!/usr/bin/env python3
"""Function with type annotations"""
from typing import Mapping, Any, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None]) -> Union[
                                                            Any,
                                                            TypeVar('T')]:
    """Returns key in a dictionary or default"""
    if key in dct:
        return dct[key]
    else:
        return default
