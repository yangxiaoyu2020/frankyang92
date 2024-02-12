#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/12 11:43
# @Author  : frank yang
# @File    : trapping_rain_water.py
# @IDE     : PyCharm
from typing import List


class TrappingRainWater:

    @staticmethod
    def trap_mon_stack(height: List[int]) -> int:
        stack = []
        length = len(height)
        ans = 0
        for i in range(length):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                top_index = stack.pop()
                if len(stack) == 0: continue
                hei = min(height[stack[-1]], height[i]) - height[top_index]
                wei = (i - stack[-1] - 1)
                ans += hei * wei
            stack.append(i)
        return ans

    @staticmethod
    def trap_dp(height: List[int]) -> int:
        ans = 0
        length = len(height)
        if length < 3: return ans
        left_dp = [0] * length
        right_dp = [0] * length
        left_dp[0] = height[0]
        right_dp[-1] = height[-1]
        for i in range(1, length):
            left_dp[i] = max(left_dp[i-1], height[i])
        for i in range(length-2, -1, -1):
            right_dp[i] = max(right_dp[i + 1], height[i])
        for i in range(length):
            ans += min(left_dp[i], right_dp[i]) - height[i]
        return ans

    @staticmethod
    def trap_two_points(height: List[int]) -> int:
        ans = 0
        max_left = 0
        max_right = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    ans += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
        return ans

    @staticmethod
    def trap_force(height: List[int]) -> int:
        ans = 0
        for i in range(len(height)-1):
            max_left = 0
            for j in range(i-1, -1, -1):
                if height[j] > max_left:
                    max_left = height[j]
            max_right = 0
            for j in range(i+1, len((height))):
                if height[j] > max_right:
                    max_right = height[j]
            min_hei = min(max_right, max_left)
            if min_hei > height[i]:
                ans += min_hei - height[i]

        return ans


if __name__ == "__main__":
    test_data = [4, 2, 0, 3, 2, 5]
    res = TrappingRainWater.trap_force(test_data)
    assert res == 9

    test_data = [4, 2, 0, 3, 2, 5]
    res = TrappingRainWater.trap_mon_stack(test_data)
    assert res == 9

    res = TrappingRainWater.trap_two_points(test_data)
    assert res == 9

    res = TrappingRainWater.trap_dp(test_data)
    assert res == 9

