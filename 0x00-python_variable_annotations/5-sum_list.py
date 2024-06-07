#!/usr/bin/env python3
"""Import List from typing"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function sum_list which takes a list input_list of floats as argument
    and returns their sum as a float.

    Args:
        input_list (list[float]): list input_list of floats from user

    Returns:
        float: return to user
    """
    sum = 0.0
    for value in input_list:
        sum += value
    return sum
