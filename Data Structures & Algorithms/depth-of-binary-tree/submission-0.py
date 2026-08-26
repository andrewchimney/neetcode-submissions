# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(depth, root) -> int:
            if(root):
                depth+=1
                d1=search(depth, root.left)
                d2=search(depth, root.right)
                return max(d1,d2)
            return depth


        depth=0
        return search(depth, root)

        