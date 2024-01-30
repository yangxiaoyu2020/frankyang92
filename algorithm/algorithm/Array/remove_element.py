#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/29 9:29
# @Author  : frank yang
# @File    : remove_element.py
# @IDE     : PyCharm
from typing import List


class RemoveElement:

    @staticmethod
    def remove_element_method_1(nums: List[int], val: int) -> int:
        # address the corner case
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == val:
            return 0
        right = len(nums)
        left = 0
        while left < right:
            if nums[left] == val:
                for j in range(left + 1, right):
                    nums[j - 1] = nums[j]
                right -= 1
                left -= 1
            left += 1
        return right

    @staticmethod
    def remove_element_method_2(nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1 and nums[0] == val:
            return 0
        slow = 0
        fast = 0
        while fast < length:
            if nums[fast] == val and fast == length - 1:
                return slow
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
