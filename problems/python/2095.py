# [AC 05/29/2024]
# 2095. Delete the Middle Node of a Linked List
# Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # My original solution
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        n = 0
        i = head
        while i.next != None:
            i = i.next
            n += 1
        
        if n % 2 != 0:
            n = n // 2
        else:
            n = n // 2 - 1
        
        i = head
        for j in range(n):
            i = i.next
        gap = i.next
        i.next = gap.next
        
        return head

class Solution: # Faster solution using 2 pointers
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        
        fast, slow = head.next.next, head

        while fast and fast.next:
            slow = slow.next # moves 1 pos
            fast = fast.next.next # moves 2 pos
        
        # at this point, slow is right before middle element of list
        # and fast has reached the end of the list
        slow.next = slow.next.next
        return head
