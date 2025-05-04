#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Truncation removed as per user request implicit in task
            # description
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of the dataset using index-based pagination,
        resilient to deletions.

        Args:
            index (int, optional): The start index of the page.
                                   Defaults to 0 if None.
            page_size (int, optional): The number of items per page.
                                      Defaults to 10.

        Returns:
            Dict: A dictionary containing pagination details:
                - index: Start index of the returned page.
                - next_index: Index of the first item after the current page.
                - page_size: The current page size.
                - data: The actual page of the dataset.
        """
        if index is None:
            index = 0

        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        # Assert index validity
        assert isinstance(index, int) and 0 <= index < total_items, \
            "Index out of valid range"
        assert isinstance(page_size, int) and page_size > 0

        page_data = []
        items_count = 0
        current_index = index
        next_idx_candidate = None

        # Use sorted keys to handle potential gaps from deletions
        sorted_keys = sorted(indexed_data.keys())

        # Find the starting position in the sorted keys list
        key_start_pos = -1
        for i, key in enumerate(sorted_keys):
            if key >= index:
                key_start_pos = i
                break

        if key_start_pos != -1:
            checked_keys = 0
            while checked_keys < page_size and \
                    key_start_pos < len(sorted_keys):
                current_key = sorted_keys[key_start_pos]
                page_data.append(indexed_data[current_key])
                checked_keys += 1
                key_start_pos += 1  # Move to the next key

            # Determine next_index
            if key_start_pos < len(sorted_keys):
                next_idx_candidate = sorted_keys[key_start_pos]
            else:
                next_idx_candidate = None  # No more items left
        else:  # Index is greater than any existing key
            next_idx_candidate = None

        return {
            "index": index,
            "data": page_data,
            "page_size": len(page_data),
            "next_index": next_idx_candidate
        }
