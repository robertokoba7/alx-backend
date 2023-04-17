#!/usr/bin/env python3
"""Implementation of a method the takes two integers args  with default value 1
"""


import csv
import math
from typing import Tuple, List


index_range = __import__("0-simple_helper_function").index_range


class Server:
    """server class to paginate the given popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the elements with a pagination order"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        res_list = []

        if start >= len(self.dataset()):
            return res_list
        res_list = self.dataset()[start:end]
        return res_list
