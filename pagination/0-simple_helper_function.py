#!/usr/bin/env python3
"""function that takes 2 integers"""


def index_range(page: int, page_size: int):
    """function that takes 2 integers"""
    a: int = page_size * page - page_size
    return [a, page_size * page]
