#!/usr/bin/python3
"""
BaseCaching module

Defines the BaseCaching class that:
    -provides constant for my caching system
    -stores my cache data in a dictionary
    -has methods for putting items from the cache
"""

from base_caching import BaseCaching
"""
contains a dictionary
"""


class BasicCache(BaseCaching):
    """
    Class where my data are stored in the dictionary
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseCaching class
        """
        self.cache_data = {}

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key))

    def put(self, key, item):
        """
        adds an item  to the cache

        -param key: the key to use to store the item
        -param item: the key to store in cache
        """
        if key is not None and item is not None:
            self.cache_data[key]=item

    def get(self, key):
        """
        Retrives the item from the cache.

        -param key: the key of the item to be retrived.
        -return: the item associated with the key, None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
