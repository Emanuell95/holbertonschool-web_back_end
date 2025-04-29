#!/usr/bin/env python3
"""
This module contains a helper function for calculating pagination indices.
"""

from typing import Tuple


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
    # Since pages are 1-indexed, subtract 1 before multiplying
    start_index = (page - 1) * page_size

    # Calculate the end index
    # It's simply the start index plus the page size
    end_index = start_index + page_size

    return (start_index, end_index)


