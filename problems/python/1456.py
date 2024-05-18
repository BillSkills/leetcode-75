# [AC 05/15/2024]
# 1456. Maximum Number of Vowels in a Substring of Given Length
# Sliding Window
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max = cur = 0

        for i in range(k):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                cur += 1
        if cur > max: max = cur
        
        for i in range(k, len(s)):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}: cur += 1
            if s[i - k] in {'a', 'e', 'i', 'o', 'u'}: cur -= 1
            if cur > max: max = cur
        
        return max