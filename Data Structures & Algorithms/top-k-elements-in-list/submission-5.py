class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in count:
            buckets[count[num]].append(num)

        ret = []
        for i in range(len(buckets)-1, 0, -1):
            for j in range(len(buckets[i])):
                ret.append(buckets[i][j])
                if len(ret)==k:
                    return ret
        