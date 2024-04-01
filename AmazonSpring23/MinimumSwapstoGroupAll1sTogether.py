class Solution:
    def minSwaps(self, data: List[int]) -> int:
        sub_array_size = min_swaps = sum(data)
        n = len(data)

        if sub_array_size == 1 or sub_array_size == 0:
            return 0

        # Compute the sum of first subarray
        sub_sum = sum(data[0: sub_array_size])
        # print(sub_sum)

        start = 0
        end = (start + sub_array_size) - 1

        while end < n:
            
            min_swaps = min(min_swaps, sub_array_size-sub_sum)
            # print(start, end, min_swaps)
            # take out the value at start index from sub_sum
            sub_sum -= data[start]
            start += 1

            # add the value at next end index
            end += 1
            if end < n:
                sub_sum += data[end]
            else:
                break
        
        return min_swaps

        