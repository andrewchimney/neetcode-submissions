class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums)//2
        left =0 
        right = len(nums)-1
        while(nums[i]!=target):
            # print(left)
            # print(i)
            # print(right)
            # print("\n")
            if(nums[i]<target):
                left=i+1
                i=(left+right)//2
            else:
                right=i-1
                i=(left+right)//2
            if(left>right):
                return -1
        return i
            