# [AC 05/08/2024]
# 334. Increasing Triplet Subsequence
# Array / String
# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = max(nums)  # store the max to ensure min is found
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                # first < second < n
                return True
        return False