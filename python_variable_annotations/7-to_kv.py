#!/usr/bin/env python3
"""takes a string and an int OR float n returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and an int OR float n returns a tuple"""
    return (k, v**2)
