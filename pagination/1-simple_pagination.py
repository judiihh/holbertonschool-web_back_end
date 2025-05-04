#!/usr/bin/env python3
"""
Module for simple pagination of baby names dataset.
"""

import csv
import math
from typing import List, Tuple


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
                print(f"Error: File {self.DATA_FILE} not found.")
                self.__dataset = []  # Return empty if file not found

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
