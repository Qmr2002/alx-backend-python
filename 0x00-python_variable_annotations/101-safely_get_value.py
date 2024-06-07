#!/usr/bin/env python3

"""A module to safely retrieve a value from a dictionary.

This module provides a function to retrieve a value from a dictionary
using a specified key. If the key does not exist, a default value is returned.

"""

from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return if
        the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found, otherwise
        the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
