class Solution:
    def fib(self, n: int) -> int:
        def rec_fib(n , memo):
            if n == 0:
                res = 0
            elif n <= 2:
                res = 1
            elif n in memo:
                res = memo[n]
            else:
                res = rec_fib(n-1, memo) + rec_fib(n-2, memo)
            memo[n] = res
            return res

        memo = {}
        return rec_fib(n, memo)
        