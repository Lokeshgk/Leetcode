class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(k):
            last_element = nums[n-1]
            for index in reversed(range(0, n-1)):
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                index -= 1
            nums[0] = last_element
            
