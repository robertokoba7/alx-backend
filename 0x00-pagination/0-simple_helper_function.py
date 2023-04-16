#!/usr/bin/env python3
"""Simple helper function"""


# This module provides support for type hints, including a variety of container types, such as Tuple.
# The Tuple type represents a fixed-size, immutable sequence of elements of possibly different types.
# It can be used to annotate the return type or parameter types of a function or method that returns or accepts a tuple.
from typing import Tuple



def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two corresponding to the range of indexes"""
    start = (page -1) * page_size
    end = start + page_size
    return (start, end)
