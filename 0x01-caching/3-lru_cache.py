#!/usr/bin/python3
"""
LRUCache module
"""

from base_caching import BaseCaching
"""
import Dictionary
"""


class LRUCache(BaseCaching):
    """LRU Cache"""

    def __init__(self):
        """Initialize the instance"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assign a key to a value"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.queue.pop(0)
            del self.cache_data[to_discard]
            print(f"DISCARD: {to_discard}")

        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """ return the value in self.cache_data."""
        value = self.cache_data.get(key, None)
        if value is not None:
            self.queue.remove(key)
            self.queue.append(key)
        return value
