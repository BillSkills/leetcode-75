# [AC 05/20/2024]
# 2215. Find the Difference of Two Arrays
# Hash Map / Set
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # sets ignore duplicate values, difference in sets
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]