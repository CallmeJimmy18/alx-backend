#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            this is the get_hyper_index method
        """
        if index is None:
            index = 0

        assert isinstance(index, int)
        assert 0 <= index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []
        index_next = index + page_size
        for val in range(index, index_next):
            if self.indexed_dataset().get(val):
                data.append(self.indexed_dataset()[val])
            else:
                val += 1
                index_next += 1

        return {
                'index': index,
                'data': data,
                'page_size': page_size,
                'next_index': index_next
                }
