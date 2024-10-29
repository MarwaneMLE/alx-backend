#!/usr/bin/python3
"""
Tasks 0. Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements a caching system
    """

    def put(self, key, item):
        """ Add an item to the cache.
        If key or item is None, do nothing.
        """
        if (key is not None) and (item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache.
        If key is None or doesn't exist, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
