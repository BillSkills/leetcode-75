# [AC 05/24/2024]
# 2390. Removing Stars From a String
# Stack
# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack += [char]
        
        return "".join(stack)