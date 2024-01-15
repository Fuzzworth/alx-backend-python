#!/usr/bin/env python3
"""
Module Docs
"""
import asyncio
from random import uniform


async def wait_random(max_delay: inti = 10) -> float:
    """
    Function Docs
    """
    random_delay: float = uniform(0, max_delay)
    asyncio.sleep(random_delay)
    return random_delay
