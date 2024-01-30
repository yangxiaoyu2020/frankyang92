#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/29 16:18
# @Author  : frank yang
# @File    : squares__sorted_array.py
# @IDE     : PyCharm
from typing import List


class SquaresOfSortedArray:

    @staticmethod
    def sorted_squares_direct(nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])

    @staticmethod
    def sorted_squares_two_points(nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
            i -= 1
        return res


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    new_nums = SquaresOfSortedArray.sorted_squares_two_points(nums)
    assert new_nums == [0, 1, 9, 16, 100]

    nums = [-4, -1, 0, 3, 10]
    new_nums = SquaresOfSortedArray.sorted_squares_direct(nums)
    assert new_nums == [0, 1, 9, 16, 100]
