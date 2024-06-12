#!/usr/bin/env python3

"""
Module to demonstrate an asynchronous generator that yields random float values
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random float values between 0 and 1.

    Yields:
        float: A random float value between 0 and 1.
    """
    for _ in range(10):
        yield random.uniform(0, 1)
        await asyncio.sleep(1)
