# [AC 05/11/2024]
# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if char in s and char == s[i]:
                i += 1
        return i == len(s)