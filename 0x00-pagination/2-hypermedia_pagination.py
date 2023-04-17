#!/usr/bin/env python3
"""
server class to paginate a dataset of popular baby names.
"""

from typing import Tuple, List, Dict, Any
import csv
import math


index_range = __import__("0-simple_helper_function")


class Server:
    """
    A class representing a server that provides pagination of a database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Initialize the dataset as None
        self.__dataset = None

        @property
        def dataset(self) -> List[List]:
            """
            If the dataset has not been loaded yet, load it from the CSV file
            """
            if self.__dataset is None:
                with open(self.DATA_FILE) as f:
                    reader = cvs.reader(f)
                    dataset = [row for row in reader]
                    # Store the dataset including the header row
                self.__dataset = dataset[1:]

            return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the elements of the dataset for the given page, with a pagination order.
        """
        # Ensure that page and page_size are positive integers
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the start and end indices of the page
        start, end = index_range(page, page_size)

        # Initialize an empty list to hold the results
        res_list = []

        # If the start index is greater than or equal to the length of the
        # dataset, return an empty list
        if start >= len(self.dataset()):
            return res_list

        # Otherwise, return the elements of the dataset for the given page
        res_list = self.dataset()
        return res_list[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary containing pagination information for the given page.
        """
        # Ensure that page and page_size are positive integers
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the total number of pages in the dataset
        total_pages = int(len(self.dataset()) / page_size)

        # Calculate the next and previous pages, if they exist
        next_page = page + 1 if (page + 1) < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return a dictionary containing pagination information
        return {
            "page_size": len(self.get_page(page, page_size)),
            "total_pages": total_pages,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page
        }
