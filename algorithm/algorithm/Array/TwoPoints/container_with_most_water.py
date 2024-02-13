#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/13 10:35
# @Author  : frank yang
# @File    : container_with_most_water.py
# @IDE     : PyCharm
from typing import List


class ContainerWithMostWater:

    @staticmethod
    def max_area(height: List[int]) -> int:
        length = len(height)
        if length < 2: return 0
        ans = 0
        left = 0
        right = length - 1
        while left < right:
            min_height = min(height[left], height[right])
            ans = max(ans, min_height * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans


if __name__ == "__main__":
    test_data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = ContainerWithMostWater.max_area(test_data)
    assert res == 49
