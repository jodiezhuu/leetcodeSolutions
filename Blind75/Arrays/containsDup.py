# Given an integer array nums,return true if any value appears 
# at least twice in the array, and return falseif every element is distinct.
# Time complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for index, val in enumerate(nums):
            if val in dict: 
                print(dict)
                return True
            else:
                dict[val] = index
        return False