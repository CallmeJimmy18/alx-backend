#!/usr/bin/env python3
""" class MRUCache """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
        inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
            Init method
        """
        super().__init__()
        self.mru_dict = OrderedDict()

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data the
            item value for the key key

            :param key
            :param item
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        self.mru_dict[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_used_k = next(iter(self.mru_dict))
            del self.cache_data[most_used_k]
            print('DISCARD: {}'.format(most_used_k))

        if len(self.mru_dict) > BaseCaching.MAX_ITEMS:
            self.mru_dict.popitem(last=False)

        self.mru_dict.move_to_end(key, False)

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        if key is None:
            return None

        if key in self.cache_data:
            self.mru_dict.move_to_end(key, False)
            return self.cache_data[key]
        else:
            return None
