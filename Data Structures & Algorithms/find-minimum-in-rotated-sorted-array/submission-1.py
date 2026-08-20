class Solution:
    def findMin(self, nums: List[int]) -> int:
        left =0
        right = len(nums)-1
        mid = (right+left)//2
        mid_2=mid-1
        while(nums[mid]>nums[mid_2]):
            if(nums[right]<nums[mid]):
                left=mid+1
                mid = (right+left)//2
                mid_2=mid-1
            else:
                right=mid-1
                mid = (right+left)//2
                mid_2=mid-1
        return nums[mid]
        