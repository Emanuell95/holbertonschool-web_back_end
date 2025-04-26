#!/usr/bin/env python3
"""
This module contains a function that returns a multiplication function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by the given multiplier.

    Args:
        multiplier: The float value to multiply by.

    Returns:
        A function that takes a float and returns the product of that float
        and the multiplier.
    """
    def multiply(x: float) -> float:
        """
        Multiplies a number by the stored multiplier.

        Args:
            x: The float to be multiplied.

        Returns:
            The product of x and the multiplier.
        """
        return x * multiplier

    return multiply