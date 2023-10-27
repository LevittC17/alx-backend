#!/usr/bin/env python3

"""
Module: 0-simple_helper_function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination
    Args: page (int): Page number (1-indexed)
    page_size (int): Number of items per page
    Returns:
    :tuple: A tuple containing the start index and end index
    """
    if page <= 0:
        start = 0
    else:
        start = (page - 1) * page_size

    end = start + page_size

    return start, end
