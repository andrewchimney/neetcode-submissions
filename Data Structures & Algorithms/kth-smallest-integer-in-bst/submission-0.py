# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # for i in range(1,k+1):
        #     print(i)
        #     print(k)
        #     print(root.val)
        #     if(i==k):
        #         return root.val
        #     if(root.left):
        #         root=root.left
        #     elif root.right:
        #         root=root.right
        i = 0
        ans = -1;
        def dfs(root):
            nonlocal i,ans
            print(i)
            if not root or ans != -1:
                return
            # if not root.left and not root.right and i==k:
            #     ans=root.val
            # elif not root.left and not root.right:
            #     i+=1
            #     print("here")
            dfs(root.left)
            i+=1
            if i==k:
                ans=root.val 
                return
            dfs(root.right)

        dfs(root)
        return ans
        

