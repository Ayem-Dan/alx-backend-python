#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified \
          max_delay, and returns the list of all delays in ascending order.

    Parameters:
    - n (int): The number of times to call wait_random().
    - max_delay (int or float): The maximum delay to wait for (inclusive)\
          in each call to wait_random(). Defaults to 10.

    Returns:
    - List[float]: A list of all delays, in ascending order.
    """
    # create a list to store the results
    results = []

    # create a list of tasks for wait_random() to be executed concurrently
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # wait for all the tasks to complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    # return the sorted list of results
    return sorted(results)
