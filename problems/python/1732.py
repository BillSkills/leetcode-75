# [AC 05/18/2024]
# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        alt = max(alt, gain[0])
        
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            alt = max(alt, gain[i])
        
        return alt