#!/usr/bin/env python3
""" pagination project"""

# Import necessary modules and functions
from typing import Tuple, List, Dict, Any
import csv
import math

# Import helper function from another module
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """

    # Define the name of the CSV file containing the dataset
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        # Load the dataset from the CSV file if it hasn't already been loaded
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        # Return the dataset
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Return the elements with a pagination order """

        # Check that the input arguments are of the correct type and value
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Determine the start and end indices for the current page
        start, end = index_range(page, page_size)

        # Return an empty list if the start index is beyond the end of the
        # dataset
        if start >= len(self.dataset()):
            return []

        # Return the elements for the current page
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ Returns a object """

        # Check that the input arguments are of the correct type and value
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the total number of pages in the dataset
        total_pages = int(len(self.dataset()) / page_size)

        # Calculate the page numbers for the next and previous pages
        next_page = page + 1 if (page + 1) < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return an object containing pagination information and the data for
        # the current page
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
