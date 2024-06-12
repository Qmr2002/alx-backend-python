#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine that measures the
total runtime of concurrently executing multiple instances of the
async_comprehension coroutine.

The measure_runtime coroutine uses asyncio.gather to run 4 instances
of async_comprehension concurrently and calculates the time taken
to complete their execution.
"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing 4 async_comprehension coroutines
    concurrently.

    This coroutine uses asyncio.gather to run 4 instances of
    async_comprehension concurrently and calculates the time taken
    to complete their execution.

    Returns:
        float: The total runtime in seconds for the concurrent execution
               of the 4 async_comprehension coroutines.
    """
    start_time = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = time()
    return end_time - start_time
