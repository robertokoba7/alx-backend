#!/usr/bin/python3
"""
an implementation of the LIFO (Last-In-First-Out) caching algorithm
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class that inherits from the BaseCaching
    """

    def __init__(self):
        """
        Implement constructor for the LIFOCache class
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Implement put method for the LIFOCache class
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print(f"DISCARD:{discard}")

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.stack.remove(key)
            self.stack.append(key)

    def get(self, key):
        """
        Implement get method for the LIFOCache class
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
