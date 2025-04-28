#!/usr/bin/env python3
"""
This module contains an asynchronous generator coroutine.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, asynchronously waits 1 second
    in each iteration, and yields a random number between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)