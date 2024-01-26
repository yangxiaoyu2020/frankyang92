#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/1/26 14:35
# @Author  : frank yang
# @File    : decorator.py
# @IDE     : PyCharm


import functools
import os
import time

import psutil


def trace_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} cost {end - start}")
        return result
    return wrapper


def trace_memory_usage(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        result = func(*args, **kwargs)
        memory_after = process.memory_info().rss
        print(f"{func.__name__} memory usage {memory_after - memory_before}")
        return result
    return wrapper
