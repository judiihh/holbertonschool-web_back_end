#!/usr/bin/env python3
"""Module that contains a type-annotated function floor"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float number.

    Args:
        n (float): The float number to floor

    Returns:
        int: The floor of the float
    """
    return math.floor(n) 