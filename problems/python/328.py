# [AC 05/30/2024]
# 328. Odd Even Linked List
# Linked List
# https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        ehead = even

        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = ehead
        return head