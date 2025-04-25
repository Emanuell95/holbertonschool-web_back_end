#!/usr/bin/env python3
"""
This module contains a function that sums a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Args:
        mxd_lst: A list of integers and floats.

    Returns:
        The sum of all elements in the list as a float.
    """
    return float(sum(mxd_lst))
