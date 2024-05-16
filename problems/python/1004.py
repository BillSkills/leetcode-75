# [AC 05/16/2024]
# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        for r in range(len(nums)):
            if nums[r] == 0: # subtract 1 from k to count flipped 0s
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1 # keep moving left ptr. until flipped 0s freed
        return r - l + 1 # returns diff in indices + 1 for length