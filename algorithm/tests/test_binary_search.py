#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/26 13:46
# @Author  : frank yang
# @File    : binary_search.py
# @IDE     : PyCharm


import random
import sys
import os
import unittest
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithm.Array.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):

    @staticmethod
    def init_test_data(exist: bool) -> (List[int], int, int):
        """
        init the test data
        :return: result, index, target
        """
        if exist:
            result = []
            index = random.randint(0, 20)
            target = random.randint(-10, 10)
            length = index * 3
            result.append(target)
            for i in range(index):
                result.insert(0, target - i - 1)
            for i in range(index + 1, length):
                result.append(target + i)
            return result, index, target
        else:
            # false test data
            return [5], -1, 1

    def test_search_close(self):
        input_array, index, target = self.init_test_data(True)

        index_actual = BinarySearch.search_close(input_array, target)

        self.assertEqual(index_actual, index)  # add assertion here
        input_array, index, target = self.init_test_data(False)
        index_actual = BinarySearch.search_close(input_array, target)

        self.assertEqual(index_actual, index)  # add assertion here

    def test_search_open(self):
        input_array, index, target = self.init_test_data(True)
        index_actual = BinarySearch.search_open(input_array, target)
        self.assertEqual(index_actual, index)  # add assertion here

        input_array, index, target = self.init_test_data(False)
        index_actual = BinarySearch.search_open(input_array, target)
        self.assertEqual(index_actual, index)  # add assertion here


if __name__ == '__main__':
    unittest.main()

