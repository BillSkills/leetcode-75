# [AC 05/17/2024]
# 1493. Longest Subarray of 1's After Deleting One Element
# Sliding Window
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 0
        size = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
            while count > 1:
                if nums[i] == 0:
                    count -= 1
                i += 1
            size = max(size, j - i)

        return size