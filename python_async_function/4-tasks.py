#!/usr/bin/env python3
"""Execute multiple asyncio tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run n random delay tasks and return delays in ascending order."""
    tasks = []
    results = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        results.append(delay)

    return results
