#!/usr/bin/env python3
""" class LIFOCache """
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
            Init method
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data the
            item value for the key key

            :param key
            :param item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.queue.pop()
            del self.cache_data[last_key]
            print('DISCARD: {}'.format(last_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        if key is None:
            return None

        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
