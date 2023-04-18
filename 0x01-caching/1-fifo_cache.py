#!/usr/bin/python3

"""
Importing the BaseCaching class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Define the class that inherits from the BaseCaching
    """

    def __init__(self):
        """
        Implement constructor for the FIFOCache class
        """

        # Call the constructor of the parent class
        super().__init__()

        # Initialize an empty list for the cache data
        self.stack = []

    def put(self, key, item):
        """
        Implemente put method for the FIFOCache class
        """
        if key is None and item is None:
            return

        # Add the item to the cache dictionary
        if key not in self.stack:
            self.stack.append(key)
        else:
            self.move_to_last_in(key)

        self.cache_data[key] = item

        # check if number of items in the cache data > maximum
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.stack[0]
            if to_discard:
                self.stack.remove(to_discard)
                del self.cache_data[to_discard]
                print(f"DISCARD: {to_discard}\n")

    def get(self, key):
        """
        Implement get method for the FIFOCache class
        """

        # Checking if key is None or if
        # it doesnt exist in cache data
        if key is none or key not in self.cache_data:
            return None
        # Return the value associated with
        # the key the cache data dictionary
        return self.cache_data[key]

    def move_to_last_in(self, key):
        """
        move an elem in first postion.
        """
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
