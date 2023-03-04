#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0\
          and max_delay seconds (inclusive) and returns it.

    Parameters:
    - max_delay (int or float): The maximum delay to wait for (inclusive).\
          Defaults to 10.

    Returns:
    - delay (float): The delay that was waited for, as a float value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
