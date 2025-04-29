#!/usr/bin/env python3
"""Module that contains a type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and num to a tuple with the string and square of the num.

    Args:
        k (str): The string to use as first element
        v (Union[int, float]): The number to square

    Returns:
        Tuple[str, float]: A tuple containing the string and squared number
    """
    return (k, float(v ** 2))
