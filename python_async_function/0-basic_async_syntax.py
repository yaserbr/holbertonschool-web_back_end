#!/usr/bin/env python3
"""Provide an asynchronous function for random delays."""

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """Wait asynchronously for a random duration and return it."""
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
