# [AC 05/DD/2024]
# 933. Number of Recent Calls
# Queue
# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.requests = deque() # double ended queue

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        self.requests.append(t)
        return len(self.requests)