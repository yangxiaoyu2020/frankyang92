#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/10 13:07
# @Author  : frank yang
# @File    : longest_substring_without_repeating_characters.py
# @IDE     : PyCharm

class LongestSubstringWithoutRepeatingCharacters:

    @staticmethod
    def length_longest_substring(s: str) -> int:
        if len(s) <= 1: return len(s)
        length = len(s)
        mem = set()
        fast = 0
        slow = 0
        ans = 0
        while fast < length:
            while s[fast] in mem:
                mem.remove(s[slow])
                slow += 1
            mem.add(s[fast])
            fast += 1
            ans = max(fast - slow, ans)
        return ans


if __name__ == "__main__":
    string = "abcabcbb"
    res = LongestSubstringWithoutRepeatingCharacters.length_longest_substring(string)
    assert res == 3
