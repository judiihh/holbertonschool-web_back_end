#!/usr/bin/env python3
"""Module that contains a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floating point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of int and floats to sum

    Returns:
        float: The sum of all numbers in the list
    """
    return float(sum(mxd_lst))
