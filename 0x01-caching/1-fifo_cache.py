#!/usr/bin/env python3

"""
Importing the BaseCaching class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Define the class that inherits
    from the BaseCaching
    """

    def __init__(self):
        """
        Implement constructor
        for the FIFOCache class
        """

        # Call the constructor of the parent class
        super().__init__()

    def put(self, key, item):
        """
        Implemente put method for the FIFOCache class
        """
        if key is None or item is None:
            return

        # check if number of items
        # in the cache data > maximum
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = list(self.cache_data.keys())[0]
            del self.cache_data[to_discard]
            print(f"DISCARD: {to_discard}\n")

        # Add the item to the cache dictionary
        self.cache_data[key] = item

    def get(self, key):
        """
        Implement get method for the FIFOCache class
        """

        # Checking if key is None or if
        # it doesnt exist in cache data
        if key is None or key not in self.cache_data:
            return None
        # Return the value associated with
        # the key the cache data dictionary
        return self.cache_data[key]
