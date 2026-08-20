class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        # print(nums)
        seen = set()
        for i in range(len(nums)):
            if(nums[i] in seen):
                continue
            seen.add(nums[i])
            left = i + 1
            right = len(nums)-1
            while(left<right):
                # print("looking for ", -nums[i])
                su = nums[left]+nums[right]
                # print(nums[left], " + ", nums[right]," = ", su)
                if(su<-nums[i]):
                    left+=1
                    while(nums[left]==nums[left-1]):
                        left+=1
                elif(su>-nums[i]):
                    right-=1
                    while(nums[right]==nums[right+1] and right>0):
                        right-=1
                else:
                    # print("match found")
                    ret.append([nums[i], nums[left], nums[right]])
                    right-=1
                    while(nums[right]==nums[right+1] and right>0):
                        right-=1
                    if(left>=right):
                        break
                    
        return ret
        