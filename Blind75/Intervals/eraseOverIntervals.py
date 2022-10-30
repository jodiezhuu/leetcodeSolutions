# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest 
# of the intervals non-overlapping.
# Time complexity: O(n * log n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        # sort array based on first element
        intervals.sort(key = lambda i : i[0])
        prevEnd = intervals[0][1]
        # compare first element of curr array with second element of prev array
        for start, end in intervals[1:]:
            if start < prevEnd:
                counter += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return counter