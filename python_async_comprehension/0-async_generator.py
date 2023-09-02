#!/usr/bin/env python3
"""a coroutine that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine that takes no arguments"""
    for Z in range(10):
        await asyncio.sleep(1)
        yield random.random()
