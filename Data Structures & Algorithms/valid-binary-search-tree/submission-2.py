# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, low, high):
            if not root:
                    return True
            if(low<root.val<high):
                
                return dfs(root.right,root.val, high) and dfs(root.left,low, root.val)
            else: 
                return False
                    



        low = float("-inf")
        high = float("inf")
        return dfs(root, low, high)

        # if(not root.left):
        #     return True
        # if(root.left.val < root.val):
        #     return self.isValidBST(root.left)
        # else:
        #     return False
        # if(not root.right):
        #     return True
        # if(root.left.right > root.val):
        #     return self.isValidBST(root.right)
        # else:
        #     return False
        # return True
        
        