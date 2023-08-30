#!/usr/bin/env python3
"""asynchronous coroutine that takes an int n eventually returns it"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes an int n eventually returns it"""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
