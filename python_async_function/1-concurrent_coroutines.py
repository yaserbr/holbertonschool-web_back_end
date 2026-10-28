#!/usr/bin/env python3
"""Run multiple asynchronous coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute random delays concurrently and return their times"""
    tasks = []
    result = []
    while n != 0:
        tasks.append(asyncio.create_task(wait_random(max_delay)))
        n -= 1

    for completed in asyncio.as_completed(tasks):
        temp = await completed
        result.append(temp)
    return result
