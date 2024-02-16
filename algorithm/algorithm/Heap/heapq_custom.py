#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/16 11:13
# @Author  : frank yang
# @File    : heapq_custom.py
# @IDE     : PyCharm
import heapq


class CustomHeap:
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        return heapq.heappop(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)


# Define a tuple subclass with custom comparison
class CustomTuple(tuple):
    def __lt__(self, other):
        # Custom comparison function considering two elements tuples
        # Compare first element
        if self[0] != other[0]:
            return self[0] < other[0]
        # If first elements are equal, compare second element in reverse order
        return self[1] > other[1]


if __name__ == "__main__":
    # Sample usage
    # Define a tuple of elements
    # items = [(5, 3, 'write code'),
    #          (5, 4, 'write code 4'),
    #          (7, 9, 'release product'),
    #          (1, 1, 'write spec'),
    #          (3, 9, 'create tests')]
    h = CustomHeap()

    # Define a tuple of elements
    items = [CustomTuple((5, 3, 'write code')),
             CustomTuple((5, 4, 'write code 4')),
             CustomTuple((7, 9, 'release product')),
             CustomTuple((1, 1, 'write spec')),
             CustomTuple((3, 9, 'create tests'))]

    # Push elements onto the heap using custom comparison function
    for item in items:
        h.push(item)

    print("Original heap:", h)
    """
    Original heap: [
    (1, 1, 'write spec'), 
    (3, 9, 'create tests'), 
    (7, 9, 'release product'), 
    (5, 3, 'write code'), 
    (5, 4, 'write code 4')]
    """

    # Pop elements to see the order
    print("Popping elements:")
    while len(h) > 0:
        print(h.pop())

    """
    Popping elements:
    (1, 1, 'write spec')
    (3, 9, 'create tests')
    (5, 4, 'write code 4')
    (5, 3, 'write code')
    (7, 9, 'release product')
    """
