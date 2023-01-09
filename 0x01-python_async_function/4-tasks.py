#!/usr/bin/env python3
"""
:return a random number between 0 and max_delay
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    :return a random number between 0 and max_delay
    :param n:
    :type n:
    :param max_delay:
    :type max_delay:
    :return: delay
    :rtype: float
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
