#!/usr/bin/env python3
"""create a funct with int n return a float"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """create a funct with int n return a float"""
    time_to_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    ending_time = time.time()
    total_timing = ending_time - time_to_start
    return total_timing / n
