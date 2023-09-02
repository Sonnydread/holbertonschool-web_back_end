#!/usr/bin/env python3
"""function that takes an int and return a asyncio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function that takes an int and return a asyncio.Task"""
    the_task = asyncio.create_task(wait_random(max_delay))
    return the_task
