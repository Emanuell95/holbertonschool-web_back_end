#!/usr/bin/env python3
"""
This module contains a helper function for pagination and a Server class
to paginate a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and end index (exclusive) for the requested page.
    """
    # Calculate the start index (0-based)
    start_index = (page - 1) * page_size
    # Calculate the end index
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Loads the dataset from the CSV file the first time it's accessed
        and caches it.

        Returns:
            List[List]: The dataset excluding the header row.
        """
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                # Cache the dataset excluding the header row
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                print(f"Error: File '{self.DATA_FILE}' not found.")
                self.__dataset = [] # Set to empty list if file not found
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed, default 1).
            page_size (int): The number of items per page (default 10).

        Returns:
            List[List]: The list of rows corresponding to the requested page.
                        Returns an empty list if arguments are invalid or
                        out of range.
        """
        # Assert that page and page_size are positive integers
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        # Get the full dataset
        dataset = self.dataset()
        # Calculate the start and end indices for pagination
        start_index, end_index = index_range(page, page_size)

        # Get the total number of rows in the dataset
        total_rows = len(dataset)

        # Check if the calculated start index is out of range
        if start_index >= total_rows:
            return []  # Return empty list if page is beyond the data

        # Return the requested slice of the dataset
        # Adjust end_index if it exceeds the dataset bounds
        return dataset[start_index:min(end_index, total_rows)]

