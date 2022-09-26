# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum 
# and return its sum.

# A subarray is a contiguous part of an array.

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