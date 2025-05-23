#!/usr/bin/env python3
"""Measure runtime of async_comprehension coroutine."""

import asyncio
import time

# Import the async_comprehension coroutine from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and measure runtime."""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
