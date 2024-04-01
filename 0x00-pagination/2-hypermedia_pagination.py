#!/usr/bin/env python3
"""
    index_range
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
       takes two integer arguments page and page_size
    """
    start_indx = (page - 1) * page_size
    end_indx = page * page_size
    return start_indx, end_indx


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Returns the page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        try:
            start_indx, end_indx = index_range(page, page_size)
            return data[start_indx:end_indx]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            returns a dictionary containing the following key-value pairs
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start_indx, end_indx = index_range(page, page_size)

        if (page < total_pages):
            next_page = page+1
        else:
            next_page = None

        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {
                'page_size': len(data)
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_page': total_pages
                }
