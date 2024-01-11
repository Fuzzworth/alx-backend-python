#!/usr/bin/env python3
'''
Module Doc
'''
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Parameters:
    - mxd_lst (List[int | float]): The list of integers and floats.

    Returns:
    float: The sum of the input list.
    """
    return float(sum(mxd_lst))
