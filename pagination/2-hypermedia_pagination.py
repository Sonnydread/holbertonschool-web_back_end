#!/usr/bin/env python3
"""index_range that takes two integers"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(iself, page: int, page_size: int) -> Tuple:
        """function that takes 2 integers"""
        a: int = page_size * page - page_size
        return (a, page_size * page)

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
        """takes two integer arguments page and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        with open(self.DATA_FILE, "r") as f:
            reader = csv.reader(f)
            datos = list(reader)
            start, end = self.index_range(page, page_size)
            page_data = data[start+1:end+1]
        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs"""
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        di = {
              "page_size": page_size if page_size <= len(info) else len(info),
              "page": page,
              "data": data,
              "total_pages": total_pages,
              "next_page": page + 1 if page + 1 <= total_pages else None,
              "prev_page": page - 1 if page > 1 else None
        }
        return di
