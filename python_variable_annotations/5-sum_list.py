#!/usr/bin/env python3
"""Module that contains a type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating point numbers.

    Args:
        input_list (List[float]): The list of floats to sum

    Returns:
        float: The sum of all numbers in the list
    """
    return sum(input_list)
