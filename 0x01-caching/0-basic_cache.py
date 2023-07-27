#!/usr/bin/env python3
"""This module defines a basic caching system."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    defines a basic caching system.
    """
    def put(self, key, item):
        """
        implements the put method.
        inserts key,value pairs in a dictionary.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        implements the get method.
        fetches a value from the cache by it's key.
        return None if the value of the key does not exist.
        """
        return self.cache_data.get(key, None)
