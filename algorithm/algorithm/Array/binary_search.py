#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/26 13:46
# @Author  : frank yang
# @File    : binary_search.py
# @IDE     : PyCharm


from typing import List

from algorithm.utils.decorator import trace_time, trace_memory_usage


class BinarySearch:
    @staticmethod
    @trace_time
    @trace_memory_usage
    def search_close(nums: List[int], target: int) -> int:
        """
        when use the close range
        for example [left, right]
        :param nums:
        :param target:
        :return: the index of the target in nums
        """
        left = 0
        right = len(nums) - 1
        if (right == 0): return 0 if nums[0] == target else -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

    @staticmethod
    @trace_time
    @trace_memory_usage
    def search_open(nums: List[int], target: int) -> int:
        """
        Another way to do the bin_search
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums)
        if (right == 0): return 0 if nums[0] == target else -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid
            elif nums[mid] < target: left = mid + 1
        return -1
