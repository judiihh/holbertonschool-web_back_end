#!/usr/bin/env python3
"""
Helper module for handling pagination calculations.
This module provides utility functions to help with implementing pagination
in a list of items, making it easier to divide data into pages and
calculate the correct start and end indexes for each page.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination parameters.
    This function takes a page number and page size, then calculates
    the appropriate start and end indexes needed to paginate a list
    of items. The calculation assumes 1-indexed page numbers.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple of two integers containing:
            - the start index (inclusive) for the items on the requested page
            - the end index (exclusive) for the items on the requested page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
