#!/usr/bin/env python3
"""
Module Docs
"""
import asyncio
from typing import Awaitable, Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[Any]:
    """
    Function Docs
    """
    return wait_random(max_delay)
