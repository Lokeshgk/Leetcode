class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # sort the intervals first
        intervals.sort(key = lambda x:x[0])

        # merge intervals
        start = 0
        merged = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
        return merged
