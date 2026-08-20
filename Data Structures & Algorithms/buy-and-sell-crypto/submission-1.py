class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(len(prices)):

            for j in range(i, len(prices)):
                ret = max(ret, prices[j]-prices[i])

        return ret