#!/usr/bin/env python3
"""
This module contains a coroutine that utilizes async comprehension
to collect values from an asynchronous generator.
"""

import asyncio
from typing import List

# Import the async_generator from the specified module
# This assumes '0-async_generator.py' exists in the same directory
# or is accessible via Python's module search path.
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over the async_generator, then returns the list of collected numbers.

    Returns:
        List[float]: A list containing 10 random floating-point numbers
                     yielded by async_generator.
    """
    # Use an asynchronous list comprehension to iterate through async_generator
    # and collect all the yielded values into a list.
    result = [i async for i in async_generator()]
    return result


