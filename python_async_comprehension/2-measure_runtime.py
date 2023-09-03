#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    rightnow = asyncio.get_event_loop()
    start_time = rightnow.time()
    mission = [async_comprehension() for Z in range(0, 5)]
    result = await asyncio.gather(*mission)
    ending = rightnow.time()
    total_time = ending - start_time
    return total_time
