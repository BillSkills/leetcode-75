# [AC 05/21/2024]
# 1207. Unique Number of Occurrences
# Hash Map / Set
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for num in arr:
            dict[num] = dict.get(num, 0) + 1
        
        return len(set(dict.values())) == len(dict.values())