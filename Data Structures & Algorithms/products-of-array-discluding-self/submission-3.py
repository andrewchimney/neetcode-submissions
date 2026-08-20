class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(len(nums)==2):
            return [nums[1],nums[0]]
        product = 1
        px0=1
        z_count=0
        for num in nums:
            if(num):
                px0*= num
            else:
                z_count+=1    
            product*= num
        li = []
        for num in nums:
            if(not num):
                if(z_count==1):
                    li.append(px0) 
                else:
                    li.append(0)     
            else:
                li.append(product//num)
        return li
        