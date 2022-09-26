# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum 
# and return its sum.

# A subarray is a contiguous part of an array.

# Time Complexity: O(n) for each, but first function has
# more efficient space complexity
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        cur_max = nums[0]
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                ## update current sum
                cur_sum += nums[i]
            ## set new maximum
            if cur_sum > cur_max:
                cur_max = cur_sum
        return cur_max

# Dynamic Programming
## dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_arr = [nums[0]]
        for i in range(1, len(nums)):
            max_arr.append(max(nums[i] + max_arr[i - 1], nums[i]))
        return max(max_arr)
    