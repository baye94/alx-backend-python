#!/usr/bin/env python3
"""
:return a random number between 0 and max_delay
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    :return a random number between 0 and max_delay
    :param max_delay:
    :type max_delay:
    :return: delay
    :rtype: float
    """
    return asyncio.create_task(wait_random(max_delay))
