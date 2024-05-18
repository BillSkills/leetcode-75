# [AC 05/12/2024]
# 11. Container With Most Water
# Two Pointers
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left and right pointers
        i = 0
        j = len(height) - 1
        max = 0 # max water stored

        while i < j:
            bound = height[i] if height[i] < height[j] else height[j]
            stored = (j - i) * bound
            if stored > max: max = stored

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max