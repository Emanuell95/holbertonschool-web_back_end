#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        """Return deletion-resilient hypermedia pagination for the dataset.
        
        Args:
            index (int, optional): Starting index of the page. Defaults to None.
            page_size (int, optional): Size of the page. Defaults to 10.
            
        Returns:
            Dict: Pagination information with keys: index, next_index, 
                  page_size, and data.
        """
        # Initialize index to 0 if None
        if index is None:
            index = 0
            
        # Get the indexed dataset
        indexed_data = self.indexed_dataset()
        
        # Verify the index is in valid range
        assert index >= 0 and index < len(self.dataset()), "Index out of range"
        
        # Collect page data accounting for deleted indices
        data = []
        curr_index = index
        items_count = 0
        
        while items_count < page_size and curr_index < len(self.dataset()):
            # If the index exists in our indexed dataset
            if curr_index in indexed_data:
                data.append(indexed_data[curr_index])
                items_count += 1
            curr_index += 1
            
        # Calculate the next index to query
        next_index = curr_index
        
        # Return the requested page data
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
        