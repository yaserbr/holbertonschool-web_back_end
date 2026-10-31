#!/usr/bin/env python3
"""Provide a coroutine that collects random numbers asynchronously."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect and return ten random floats from async_generator."""
    return [number async for number in async_generator()]
