# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        curr = head
        while curr:
            curr=curr.next
            i+=1

        curr = head
        n=i-n
        if(n==0):
            return head.next
            
        # print("n: ", n)
        i = 0
        while curr:
            if(i==(n-1)):
                if(curr.next):
                    temp=curr.next
                else:
                    # print("here1")
                    return None
                if(temp.next):
                    temp=temp.next
                else:
                    # print("here2")
                    curr.next=None
                    return head
                # print(curr.val)
                curr.next=temp
                break
            # print(i, curr.val)
            curr=curr.next
            i+=1

        return head
        