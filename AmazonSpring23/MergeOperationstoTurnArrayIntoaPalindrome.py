class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        min_operation = 0

        while start < end:
            if nums[start] == nums[end]:
                start += 1
                end -= 1

            elif nums[start] < nums[end]:
                nums[start + 1] = nums[start] + nums[start + 1]
                start += 1
                min_operation += 1
            
            elif nums[start] > nums[end]:
                nums[end - 1] = nums[end] + nums[end - 1]
                end -= 1
                min_operation += 1
        
        return min_operation


        