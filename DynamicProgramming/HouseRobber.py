class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        maxRobbed = [0] * (n + 1) 
        maxRobbed[n] = 0
        maxRobbed[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            maxRobbed[i] = max(maxRobbed[i+1], maxRobbed[i+2]+nums[i])
        
        return maxRobbed[0]

        