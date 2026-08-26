# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint
        slow = head
        fast = head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        half_1 = head
        half_2 = slow.next
        slow.next=None

        prev = None
        curr = half_2

        while(curr):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        half_2=prev

        temp = None
        while(half_1 and half_2):
            nxt=half_1.next
            half_1.next = half_2
            temp=half_2.next
            half_2.next=nxt
            half_2=temp
            half_1=nxt

        
        