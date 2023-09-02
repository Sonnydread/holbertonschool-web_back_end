#!/usr/bin/env python3
"""This code is nearly identical to wait_n"""
import asyncio
import typing
from typing import List
wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This code is nearly identical to wait_n"""
    delay = []
    numbs = [wait_random(max_delay) for x in range(n)]
    done = asyncio.as_completed(numbs)
    for S in done:
        wait = await S
        delay.append(wait)

    return sorted(delay)
