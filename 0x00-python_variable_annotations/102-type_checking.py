#!/usr/bin/env python3

"""A module to zoom in on elements of a tuple by repeating them.

This module provides a function to create a list where each element
of the input tuple is repeated a specified number of times.

"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Repeat each element of the tuple a specified number of times.

    Args:
        lst (Tuple): The input tuple whose elements are to be repeated.
        factor (int, optional): The number of times to repeat each element.
        Defaults to 2.

    Returns:
        List: A list containing the elements of the input tuple repeated
        the specified number of times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Example usage
array = (12, 72, 91)

zoom_2x = zoom_array(array)
"""A list where each element from `array` is repeated 2 times."""

zoom_3x = zoom_array(array, 3)
"""A list where each element from `array` is repeated 3 times."""
