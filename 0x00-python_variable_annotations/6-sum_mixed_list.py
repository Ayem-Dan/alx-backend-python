#!/usr/bin/env python3
""" This scripts contains a functon that takes a list of floats
and integers and adds them """
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """returns float as a string"""
    return sum(mxd_lst)
