#!/usr/bin/env python3
"""
Module Docs
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Function Docs
    """
    list_of_delays = []
    for _ in range(n):
        list_of_delays.append(await wait_random(max_delay))
    await sorted(list_of_delays)
    return list_of_delays
