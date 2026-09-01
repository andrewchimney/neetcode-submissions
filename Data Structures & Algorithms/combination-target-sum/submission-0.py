class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, currentList, total):
            if total==target:
                result.append(currentList.copy())
                return
            if (i+1>len(nums)) or (total>target):
                return
            currentList.append(nums[i])
            total+=nums[i]
            dfs(i, currentList, total)
            total-=currentList.pop()
            dfs(i+1, currentList, total)
        dfs(0,[],0)
        return result
            
            

        