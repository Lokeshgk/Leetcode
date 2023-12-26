class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def cal_ways(n, memo):
            if n == 1:
                res = 1
                return res
            elif n == 2:
                res = 2
                return res
            elif n in memo:
                res = memo[n]
            else:
                res = cal_ways(n-1, memo) + cal_ways(n-2, memo)
            memo[n] = res
            return res
        
        return cal_ways(n, memo)
