#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/30 14:48
# @Author  : frank yang
# @File    : minimum_size_subarray_sum.py
# @IDE     : PyCharm
import random
from typing import List

from algorithm.utils.decorator import trace_memory_usage, trace_time


class MinimumSizeSubarraySum:

    @staticmethod
    @trace_time
    @trace_memory_usage
    def min_sub_array_sum(target: int, nums: List[int]) -> int:
        length = len(nums)
        sum_before = sum(nums)
        if sum_before < target:
            return 0
        if sum_before == target:
            return length
        if length == 1:
            return 1 if nums[0] >= target else 0
        left = 0
        right = 0
        result = length + 1
        # ? this part is to cal the case which has no right result
        # 1 <= nums[i] <= 10^4
        sum_nums = 0

        while right < length:
            sum_nums += nums[right]
            while sum_nums >= target:
                result = min(result, right - left + 1)
                sum_nums -= nums[left]
                left += 1
            right += 1
        return 0 if result == length + 1 else result


if __name__ == "__main__":
    target = random.randint(1, 1000)
    nums = []
    for i in range(100000):
        nums.append(random.randint(1, 1000))
    res = MinimumSizeSubarraySum.min_sub_array_sum(target, nums)
    print(res)
