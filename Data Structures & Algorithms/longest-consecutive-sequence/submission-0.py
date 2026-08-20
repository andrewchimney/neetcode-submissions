class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        print(s)
        ret=0
        for num in s:
            count=1
            if(num-1 not in s):
                while(num+1 in s):
                    count+=1
                    num+=1
                ret = max(ret,count)
        return ret