#!/usr/bin/env python3
'''
Module Docs
'''


def sum_list(input_list: list[float]) -> float:
    result: float = 0.0
    for i: float in input_list:
        result += i
    return result;
