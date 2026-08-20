class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [0] * len(nums)
        suffix_product = [0] * len(nums)
        for i in range(len(nums)):
            if(i==0):
                prefix_product[0]=1
                continue
            prefix_product[i]=prefix_product[i-1]*nums[i-1]
        # print(prefix_product)

        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                suffix_product[len(nums)-1]=1
                continue
            suffix_product[i]=suffix_product[i+1]*nums[i+1] 

        # print(suffix_product)
        li=[0]*len(nums)
        for i in range(len(nums)):
            li[i]=(prefix_product[i]*suffix_product[i])
        return li
        