#!/usr/bin/env python3
"""
This module contains a function that creates a tuple from a string and a number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of a number.

    Args:
        k: A string to be used as the first element of the tuple.
        v: An integer or float to be squared.

    Returns:
        A tuple where the first element is the string k and the second
        element is the square of v as a float.
    """
    return (k, float(v ** 2))
