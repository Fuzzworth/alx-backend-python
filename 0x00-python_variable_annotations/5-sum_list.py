#!/usr/bin/env python3
'''
Module Docs
'''


def sum_list(input_list: list[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Parameters:
    - input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the input list.
    """
    result: float = 0.0
    for i in input_list:
        result += i
    return result
