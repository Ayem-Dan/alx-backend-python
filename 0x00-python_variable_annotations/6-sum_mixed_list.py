#!/usr/bin/env python3
import typing
""" This scripts contains a functon that takes a float
then returns the string representation """


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float, int]]) -> float:
    # returns flpat as a string
    return sum(mxd_lst)
