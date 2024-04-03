#!/usr/bin/env python3
""" class LRUCache """
from typing import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
            Init method
        """
        super().__init__()
        self.lru_data = OrderedDict()

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data the
            item value for the key key

            :param key
            :param item
        """
        if key and item:
            self.lru_data[key] = item
            self.lru_data.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_used_k = next(iter(self.lru_data))
            del self.cache_data[least_used_k]
            print('DISCARD:', least_used_k)

        if len(self.lru_data) > BaseCaching.MAX_ITEMS:
            self.lru_data.popitem(last=False)

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        if key is None:
            return None

        if key in self.cache_data:
            self.lru_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
