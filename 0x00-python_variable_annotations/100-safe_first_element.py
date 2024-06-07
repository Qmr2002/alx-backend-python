#!/usr/bin/env python3

"""A module to safely retrieve the first element of a sequence.

This module provides a function to retrieve the first element
of a given sequence if it exists, otherwise it returns None.

"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence from which the first element
        will be retrieved.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
