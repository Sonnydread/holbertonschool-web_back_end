#!/usr/bin/env python3
"""takes a float and return a funct taht multiplies a float"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """takes a float and return a funct taht multiplies a float"""
    def make_return(x: float) -> float:
        """takes a float and return a funct taht multiplies a float"""
        return x * multiplier
    return make_return
