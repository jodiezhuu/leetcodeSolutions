# Time complexity: O(n); n is the length of the 2d arr
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort interval based on first element 
        intervals.sort(key = lambda i : i[0])
        # set first elemtnof res to be first subarray (since we know it has the smallest first el)
        res = [intervals[0]]
        # compare prev end element with curr start -> if start >= prev end then append the max of end and prev end
        for currStart, currEnd in intervals[1:]:
            prevEnd = res[-1][1]
            if (currStart <= prevEnd):
                res[-1][1] = max(prevEnd, currEnd)
        # else: append regualr start and end array
            else:
                res.append([currStart, currEnd])
        return res