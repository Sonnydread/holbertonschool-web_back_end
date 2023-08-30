#!/usr/bin/env python3
"""takes a list of int n floats and returns their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of int n floats and returns their sum as a float"""
    return sum(mxd_lst)
