#!/usr/bin/env python3
"""Module that contains an async generator function"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields a random number between 0 and 10 every second,
    10 times in total.

    Returns:
        Generator yielding random float numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
