# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr:
                return
            temp = curr.left
            curr.left=curr.right
            curr.right=temp
            reverse(curr.left)
            reverse(curr.right)
        curr=root
        reverse(curr)

        return root
