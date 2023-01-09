#!/usr/bin/env python3
"""
:return the time it takes to wait for n tasks to complete
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    :param n:
    :type n:
    :param max_delay:
    :type max_delay:
    :return: delay
    :rtype: float
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return time.time() - start
