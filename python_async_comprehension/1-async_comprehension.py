#!/usr/bin/env python3
"""Async comprehension over async_generator to collect random numbers."""

# Import the async_generator coroutine from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Collect 10 random numbers using an async comprehension over async_generator."""
    return [number async for number in async_generator()]
