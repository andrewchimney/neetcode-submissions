# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        cur1 = list1
        cur2 = list2
        head = ret
        if(not(list1 or list2)):
            return None
        if(not list2):
            ret=list1
            cur1=cur1.next
        elif(not list1):
            ret=list2
            cur2=list2.next
        elif(list1.val<list2.val):
            ret=list1
            cur1=cur1.next
        else:
            ret=list2
            cur2=list2.next
        head = ret
        while cur1 and cur2:
            if(cur1.val>=cur2.val):
                ret.next=cur2
                cur2=cur2.next
            elif(cur2.val>=cur1.val):
                ret.next=cur1
                cur1=cur1.next
            ret=ret.next
        while(cur1):
            ret.next=cur1
            ret = ret.next
            cur1=cur1.next
        while(cur2):
            ret.next=cur2
            ret = ret.next
            cur2=cur2.next
        return head

        