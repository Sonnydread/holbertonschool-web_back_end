#!/usr/bin/env python3
"""List of floats"""
from typing import List


def sum_list(input_list: typing.List[float]) -> float:
    """takes a list of floats and return their sum as a float"""
    add = 0
    for S in input_list:
        add += S
    return add
