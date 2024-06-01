# [AC 06/01/2024]
# 2130. Maximum Twin Sum of a Linked List
# Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first = twin = head

        # move twin pointer to middle of list
        while first:
            first = first.next.next
            twin = twin.next
        first = head

        # reverse second half of list
        node = None
        while twin:
            temp = twin.next
            twin.next = node
            node = twin
            twin = temp
        twin = node

        # calculate max twin sum
        sum = 0
        while twin:
            sum = max(sum, first.val + twin.val)
            first = first.next
            twin = twin.next
        
        return sum