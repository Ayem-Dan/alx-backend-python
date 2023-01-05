#!/usr/bin/env python3
"""Corrected duck-typed annotations """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element in a list"""
    if lst:
        return lst[0]
    else:
        return None
