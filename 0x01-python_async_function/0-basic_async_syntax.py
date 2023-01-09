#!/usr/bin/env python3
"""
:return a random number between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    :return a random number between 0 and max_delay
    :param max_delay:
    :type max_delay:
    :return: delay
    :rtype: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
