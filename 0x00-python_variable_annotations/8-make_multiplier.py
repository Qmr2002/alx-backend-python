#!/usr/bin/env python3

"""A module to create multiplier functions.

This module provides a function to create multiplier functions.
Given a multiplier, it returns a function that multiplies its input
by the provided multiplier.

"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function.

    Args:
        multiplier (float): The multiplier value to multiply with.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the result of multiplying it by the given multiplier.
    """
    def multiply(value: float) -> float:
        """Multiply a value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the value by the multiplier.
        """
        return value * multiplier
    return multiply
