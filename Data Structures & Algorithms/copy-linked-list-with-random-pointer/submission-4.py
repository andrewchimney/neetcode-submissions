"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head):
             return None
        head_new = Node(head.val, None, head.random)
        curr = head
        curr_new = head_new
        curr=curr.next

        ha={}
        ha[head]=head_new
        while curr:

            curr_new.next = Node(curr.val, None, None)
            curr_new=curr_new.next
            ha[curr]=curr_new
            curr=curr.next
            
        # print(ha)

        curr_new = head_new
        curr = head
        while curr_new:
            if(curr.random==None):
                curr_new.random=None
            else:
                curr_new.random = ha[curr.random] 
            curr=curr.next
            curr_new=curr_new.next

        return head_new

        