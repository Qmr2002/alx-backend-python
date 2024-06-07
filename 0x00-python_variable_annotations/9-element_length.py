#!/usr/bin/env python3

"""A module to calculate the length of elements in an iterable of sequences.

This module provides a function to calculate the length of elements
in an iterable of sequences and return them as a list of tuples,
where each tuple contains the original element and its length.

"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of elements in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        the original element from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
