#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/6 19:11
# @Author  : frank yang
# @File    : maximal_square.py
# @IDE     : PyCharm
from typing import List

from algorithm.utils.decorator import trace_time, trace_memory_usage


class MaximalSquare:
    """
    Given an m X n binary matrix filled with 0 and 1, find the largest square containing only 1
    and return its area
    """

    @staticmethod
    @trace_time
    @trace_memory_usage
    def maximal_square_direct(matrix: List[List[str]]) -> int:
        """
        the binary matrix filled with

         the 0 an 1
        :param matrix:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_side = 0
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":

                    max_side = max(max_side, 1)
                    current_max_side = min(rows - i, cols - j)
                    for k in range(1, current_max_side):
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            max_side = max(max_side, k + 1)
                        else:
                            break

        return max_side * max_side

    @staticmethod
    @trace_time
    @trace_memory_usage
    def maximal_square_dp(matrix: List[List[str]]) -> int:
        ans = 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return ans
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    if matrix[i][j] == "1":
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif matrix[i][j] == "1":
                    # this is what we should be very careful.
                    # If we use "if matrix[i][j] == "1"" we maybe re-calculate the case
                    # matrix = [["1"]], we can use this case to validate
                    dp[i][j] = min(dp[i-1][j],
                                   dp[i][j-1],
                                   dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j]*dp[i][j])
        return ans






if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    result = MaximalSquare.maximal_square_direct(matrix)
    print(result)
    result = MaximalSquare.maximal_square_dp(matrix)
    assert result == 4
    matrix = [["1"]]
    result = MaximalSquare.maximal_square_dp(matrix)
    print(result)



    need_test_big_matrix = True

    if need_test_big_matrix:
        big_matrix = []
        with open("maximal_square.txt") as f:
            """
            maximal_square_direct memory usage 24576
            maximal_square_direct cost 62.22775483131409
            """
            raw_input = f.readlines()
            matrix_line = []
            for line in raw_input:
                for c in line:
                    if c == "1":
                        matrix_line.append(c)
                    elif c == ']':
                        if matrix_line:
                            big_matrix.append(matrix_line)
                        matrix_line = []
            result = MaximalSquare.maximal_square_direct(big_matrix)
            print(result)
            result = MaximalSquare.maximal_square_dp(big_matrix)
            print(result)
            """
            maximal_square_direct memory usage 57344
            maximal_square_direct cost 55.99699544906616
            90000
            maximal_square_dp memory usage 339968
            maximal_square_dp cost 0.03350019454956055
            90000
            """