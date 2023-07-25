#!/usr/bin/env python3
"""This module defines a simple helper function."""


def index_range(page: int, page_size: int) -> tuple:
    """
    This function returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in
    a list for those particular pagination parameters.
    """
    if page == 1:
        return (0, page_size)
    page = page * 10
    page_size = page + page_size
    return (page, page_size)
