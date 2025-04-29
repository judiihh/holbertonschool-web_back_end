#!/usr/bin/env python3
"""Module that contains an async comprehension function"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[float]: List of 10 random float numbers
    """
    return [number async for number in async_generator()]
