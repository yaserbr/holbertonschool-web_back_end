#!/usr/bin/env python3
"""Provide an asynchronous function for random delays."""

import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay) -> list:
    """Wait asynchronously for a random duration and return it."""
    tasks = []
    result = []
    while n != 0:
        tasks.append(asyncio.create_task(wait_random(max_delay)))
        n -= 1

    for completed in asyncio.as_completed(tasks):
        temp = await completed
        result.append(temp)
    return result
