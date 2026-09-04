class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(i):

            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = recurse(i+1) + recurse(i+2)
            return memo[i]

            # if i+1<=n:
            #     memo[i+1]+=1
            #     recurse(i+1)
            # if i+2<=n:
            #     memo[i+2]+=1
            #     recurse(i+2)
            # # temp = memo[n]
            # # temp.append(1)
            # # memo[n+1]=temp
            # # temp = memo[n]
            # # temp.append(2)
            # # memo[n+2]=temp

        return recurse(0)
        




