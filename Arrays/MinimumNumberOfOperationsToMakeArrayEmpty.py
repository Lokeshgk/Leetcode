class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i in range(0, n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        count = 0
        for key, value in freq.items():
            if value == 1:
                return -1
            count += math.ceil(value/3)
        return count
