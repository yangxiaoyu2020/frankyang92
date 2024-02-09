#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/8 15:02
# @Author  : frank yang
# @File    : maximal_rectangle.py
# @IDE     : PyCharm


from typing import List


class MaximalRectangle:
    @staticmethod
    def maximal_rectangle(matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largest_rectangle_area(heights: List[int]) -> int:
            stack = []
            max_area = 0
            heights.append(0)  # Append 0 to handle the case where the heights end in a non-zero value
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area

        max_area = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for j in range(len(row)):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            max_area = max(max_area, largest_rectangle_area(heights))

        return max_area


if __name__ == "__main__":
    # Example usage:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(MaximalRectangle.maximal_rectangle(matrix))  # Output should be 6
