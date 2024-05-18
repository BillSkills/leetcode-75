# [AC 05/13/2024]
# 1679. Max Number of K-Sum Pairs
# Two Pointers
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1
        ops = 0

        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                ops += 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        
        return ops