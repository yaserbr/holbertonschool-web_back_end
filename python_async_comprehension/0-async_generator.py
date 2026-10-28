#!/usr/bin/env python3
"""Provide an asynchronous generator for random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random floats with a one-second delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
