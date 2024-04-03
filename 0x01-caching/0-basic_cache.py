#!/usr/bin/env python3
""" class BasicCache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
            Init method
        """
        super().__init__()

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key key

            :param key
            :param item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

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
