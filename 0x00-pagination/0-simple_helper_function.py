#!/usr/bin/env python3
"""Simple helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two corresponding to the range of indexes"""
    start = (page -1) * page_size
    end = start + page_size
    return (start, end)
