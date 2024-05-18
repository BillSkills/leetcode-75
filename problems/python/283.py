# [AC 05/10/2024]
# 283. Move Zeroes
# Two Pointers
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        # move all nonzeroes to left
        for right in range(len(nums)):
            if nums[right] != 0:
                # swap values at left and right ptrs.
                nums[right], nums[left] = nums[left], nums[right]
                left += 1 # increment left ptr, like 'wall' in quicksort partition