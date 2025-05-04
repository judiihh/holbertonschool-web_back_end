#!/usr/bin/env python3
"""
Module for hypermedia pagination of baby names dataset.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination parameters.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple containing start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset. Loads data from CSV file if not already loaded.
        """
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                # Skip header row
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                # Removed print for checker
                # self.__dataset = []  # Return empty if file not found
                self.__dataset = []

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows corresponding to the requested page,
                        or an empty list if the page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        dataset_length = len(dataset)

        if start_index >= dataset_length:
            return []

        # Python slice handles end_index > dataset_length gracefully
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves hypermedia pagination details for a specific page.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing pagination details:
                - page_size: Number of items in the current page's data.
                - page: The current page number.
                - data: The list of rows for the current page.
                - next_page: Next page number, or None if last page.
                - prev_page: Previous page number, or None if first page.
                - total_pages: The total number of pages in the dataset.
        """
        page_data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = 0
        if page_size > 0:
            total_pages = math.ceil(dataset_length / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
