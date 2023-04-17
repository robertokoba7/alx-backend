#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        # If the dataset has not been loaded yet, load it from the CSV file
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        # If the indexed dataset has not been created yet, create it from the
        # dataset
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ return all data"""
        # Ensure that the index and page_size parameters are integers
        assert isinstance(index, int) and isinstance(page_size, int)
        # Ensure that the index is within the range of the indexed dataset
        assert 0 <= index < len(self.indexed_dataset())

        data = []
        next_index = index + page_size

        # Iterate over the indices within the range of the requested page
        for i in range(index, next_index):
            if self.indexed_dataset().get(i):
                # If the element at the current index exists, append it to the
                # results list
                data.append(self.indexed_dataset()[i])
            else:
                # If the element at the current index does not exist, increment
                # the index and next_index
                i += 1
                next_index += 1

        # Return a dictionary containing the results and pagination information
        return {
            'data': data,
            'index': index,
            'next_index': next_index,
            'page_size': page_size
        }
