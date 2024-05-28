# [AC 05/28/2024]
# 649. Dota2 Senate
# Queue
# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = []
        dir = []

        for i in range(n):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dir.append(i)
        
        while rad and dir:
            if rad.pop(0) < dir.pop(0):
                rad.append(n)
            else:
                dir.append(n)
            n += 1
        
        return "Radiant" if rad else "Dire"