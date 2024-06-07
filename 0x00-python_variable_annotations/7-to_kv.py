#!/usr/bin/env python3
"""import Tuple and Union from typing
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v and
    should be annotated as a float.

    Args:
        k (str): given from main
        v (Union[int, float]): given from main

    Returns:
        Tuple[str, float]: return to main
    """
    return (str(k), float(v) ** 2)
