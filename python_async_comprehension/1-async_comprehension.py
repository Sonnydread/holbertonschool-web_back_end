#!/usr/bin/env python3
"""write a coroutine that takes no arguments"""
import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """write a coroutine that takes no arguments"""
    done = [X async for X in async_generator()]
    return result
