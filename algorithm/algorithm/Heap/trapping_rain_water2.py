#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/16 10:42
# @Author  : frank yang
# @File    : trapping_rain_water2.py
# @IDE     : PyCharm
import heapq
from typing import List


class TrappingRainWaterII:

    def trap_rain_water_heap(self, height_map: List[List[int]]) -> int:
        if len(height_map) < 3 or len(height_map[0]) < 3:
            return 0
        m, n = len(height_map), len(height_map[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if self.in_bound(i, j, m, n):
                    visited[i][j] = 1
                    heapq.heappush(pq, (height_map[i][j], i * n + j))

        res = 0
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            height, position = heapq.heappop(pq)
            for k in range(4):
                nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
                if m > nx >= 0 == visited[nx][ny] and 0 <= ny < n:
                    if height > height_map[nx][ny]:
                        res += height - height_map[nx][ny]
                    visited[nx][ny] = 1
                    heapq.heappush(pq, (max(height, height_map[nx][ny]), nx * n + ny))
        return res

    @staticmethod
    def in_bound(x, y, row, col):
        if x == 0 or y == 0 or x == row - 1 or y == col - 1:
            return True
        return False


if __name__ == "__main__":
    heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]

    ans = TrappingRainWaterII().trap_rain_water_heap(heightMap)
    assert ans == 4
