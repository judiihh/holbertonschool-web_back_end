#!/usr/bin/env python3
"""Module that contains a type-annotated function element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input iterable.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences

    Returns:
        List[Tuple[Sequence, int]]: List of tuples with each sequence and its length
    """
    return [(i, len(i)) for i in lst]
