#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/2 16:46
# @Author  : frank yang
# @File    : longest_palindromic_substring.py
# @IDE     : PyCharm
import pprint


class LongestPalindromicSubstring:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        length = len(s)
        ans = ''
        dp = [[False for _ in range(length)] for _ in range(length)]
        for i in range(length-1, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


if __name__ == "__main__":
    s = "aba"
    res = LongestPalindromicSubstring.dp_method(s)
    assert res == "aba"

