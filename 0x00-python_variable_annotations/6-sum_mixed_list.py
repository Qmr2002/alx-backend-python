#!/usr/bin/env python3
"""typing imported"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """function sum_mixed_list which takes a list mxd_lst of integers and
    floats
    and returns their sum as a float.

    Args:
        mxd_lst (list[typing.Union[int, float]]):  list mxd_lst of integers and
        floats

    Returns:
        float: returns list sum as a float
    """
    sum = 0.0
    for value in mxd_lst:
        sum += value
    return sum
