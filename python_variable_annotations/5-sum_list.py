#!/usr/bin/env python3
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all float values in the input list.

    Args:
        input_list: A list of float values.

    Returns:
        The sum of all float values in the input list.

    Raises:
        TypeError: If the input is not a list or if the list contains non-float values.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")

    total = 0.0
    for value in input_list:
        if not isinstance(value, float):
            raise TypeError("All elements in the list must be floats")
        total += value

    return total

