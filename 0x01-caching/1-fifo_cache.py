#!/usr/bin/env python3
"""defines a basic fifo cache system."""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    defines a simple fifo caching system.
    """
    def __inti__(self):
        """initialize cache storage"""
        super().__init()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """implements a put system.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                d_item = list(self.cache_data.keys())[0]
                del (self.cache_data[d_item])
                print(f'Discard: {d_item}')

    def get(self, key):
        """
        returns the value linked to the key.
        returns None if the key or the value doesn't exist.
        """
        return self.cache_data.get(key, None)
