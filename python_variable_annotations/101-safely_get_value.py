#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, TypeVar, Union, Any


TV = TypeVar("TV")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TV, None] = None) -> Union[Any, TV]:
    """Return value of the dicctionary or None"""
    if key in dct:
        return dct[key]
    else:
        return default
