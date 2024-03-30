class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_arr = [True]*len(candies)

        max_candies = max(candies)

        for i in range(0, len(candies)):
            if candies[i] + extraCandies < max_candies:
                bool_arr[i] = False
        
        return bool_arr
