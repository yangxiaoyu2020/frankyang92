#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/29 11:07
# @Author  : frank yang
# @File    : remove_duplicates_sorted.py
# @IDE     : PyCharm
from typing import List


class RemoveDuplicatesSortedArray:

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        length = len(nums)

        if length <= 1:
            return length
        slow = 1
        fast = 1
        while fast < length:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == "__name__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = RemoveDuplicatesSortedArray.remove_duplicates(nums)
    assert length == 5
    assert [0, 1, 2, 3, 4] == nums[:5]
