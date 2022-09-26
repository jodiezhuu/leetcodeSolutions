# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# Time complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefixVal = 1
        postFix = 1
        length = len(nums)
        for i in range(length):
            prefix.append(prefixVal)
            prefixVal *= nums[i]            
        for i in range(length - 1, -1, -1): ## range(start, end, step)
            prefix[i] *= postFix
            postFix *= nums[i]
        return prefix