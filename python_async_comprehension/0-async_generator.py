#!/usr/bin/env python3
"""
Module for async generator task
"""
import asyncio
import random
from typing import Generator, AsyncGenerator, List, float


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10
    with a 1 second delay between each yield
    
    Returns:
        AsyncGenerator: yields random float numbers between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        