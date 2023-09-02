#!/usr/bin/env python3
"""a coroutine that takes no argumnets"""
import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """a coroutine that takes no argumnets"""
    done = [i async for i in async_generator()]
    return done
