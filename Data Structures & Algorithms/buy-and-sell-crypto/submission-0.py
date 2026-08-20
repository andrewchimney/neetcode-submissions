class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(len(prices)):
            print(prices[i])

            for j in range(i, len(prices)):
                ret = max(ret, prices[j]-prices[i])

        return ret