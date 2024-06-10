#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(
    n: int, max_delay: int
) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
        and returns the list of all the delays (float values)."""
    delays = await asyncio.gather(*(
        wait_random(max_delay) for _ in range(n)
    ))

    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key

    return delays
