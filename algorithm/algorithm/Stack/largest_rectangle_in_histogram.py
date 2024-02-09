#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/8 17:37
# @Author  : frank yang
# @File    : largest_rectangle_in_histogram.py
# @IDE     : PyCharm
from typing import List


class LargestRectangleInHistogram:

    @staticmethod
    def largest_rectangle_histogram(heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        # in case that the all elements are increasing
        # Append 0 to handle the case where the heights end in a non-zero value


        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                # this part is the key point
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    area = LargestRectangleInHistogram.largest_rectangle_histogram(heights)
    print(area)
    assert area == 10

    heights = [2, 4]
    area = LargestRectangleInHistogram.largest_rectangle_histogram(heights)
    print(area)
    assert area == 4

    heights = [1, 1]
    area = LargestRectangleInHistogram.largest_rectangle_histogram(heights)
    print(area)
    assert area == 2
