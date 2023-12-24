class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        pointer = 0
        max_len = 0
        visited = {}
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        # iterate until the end of the string
        while pointer < len(s):
            if s[pointer] in visited:
                visited[s[pointer]] += 1
                while visited[s[pointer]] > 1:
                    visited[s[start]] -= 1
                    start += 1
            else:
                # keep track of visited elements
                visited[s[pointer]] = 1
            
            # check the maximum length substring
            max_len = max(max_len, (pointer - start) + 1)
            pointer += 1
        return max_len
        