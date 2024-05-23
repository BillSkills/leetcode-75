# [AC 05/23/2024]
# 2352. Equal Row and Column Pairs
# Hash Map / Set
# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cols = []
        for i in range(n):
            cols.append([])
            for j in range(n):
                cols[i].append(grid[j][i])
    
        pairs = 0
        for i in grid:
            for j in cols:
                if i == j: pairs += 1

        return pairs