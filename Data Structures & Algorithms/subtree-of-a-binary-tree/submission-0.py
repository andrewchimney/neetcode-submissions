# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(root, subRoot):
            if(not root and not subRoot):
                return True
            if(not root or not subRoot):
                return False
            return (
                root.val == subRoot.val
                and check(root.left, subRoot.left)
                and check(root.right, subRoot.right)
            )
            # if (root.left and subRoot.left and root.left.val==subRoot.left.val and root.right and subRoot.right and root.right.val==subRoot.right.val and root.val==subRoot.val ):
        if not root:
            return False
        if check(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        return False
        