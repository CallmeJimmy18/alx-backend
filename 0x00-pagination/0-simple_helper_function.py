#!/usr/bin/env python3
"""
    index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
       takes two integer arguments page and page_size
    """
    start_indx = (page - 1) * page_size
    end_indx = page * page_size
    return start_indx, end_indx
