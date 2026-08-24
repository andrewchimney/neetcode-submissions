# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder=0
        curr = l1
        curr_2= l2
        car=0
        su =curr.val+curr_2.val+car
        ad=su%10
        car=su//10
        ret = ListNode(ad, None)
        curr_ret = ret
        curr=curr.next
        curr_2=curr_2.next
        while curr and curr_2:
            su =curr.val+curr_2.val+car
            ad=su%10
            car=su//10
            curr_ret.next = ListNode(ad, None)
            curr=curr.next
            curr_2=curr_2.next
            curr_ret=curr_ret.next
        while(curr):
            su =curr.val+car
            ad=su%10
            car=su//10
            curr_ret.next = ListNode(ad, None)
            curr_ret=curr_ret.next
            curr=curr.next
        while(curr_2):
            su =curr_2.val+car
            ad=su%10
            car=su//10
            curr_ret.next = ListNode(ad, None)
            curr_ret=curr_ret.next
            curr_2=curr_2.next
        if(car):
            curr_ret.next = ListNode(car, None)
        return ret


        