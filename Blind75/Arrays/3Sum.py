# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize array
        arr = []
        # sort array
        nums.sort() ## O(n * log n)
        # check for each negative number possibility as first element in subarray
        # use two sum algo with target of the negative number 
        index = 0
        length = len(nums) - 1
        while (index <= length - 2):
            if nums[index] <= 0:
                target = nums[index]
            else:
                break
                
            if (index != 0) and (nums[index] == nums[index - 1]):
                index += 1
                continue
                
            low = index + 1
            high = length
            while (high > low):
                sum = nums[low] + nums[high] + target
                if (low != index + 1) and (nums[low] == nums[low - 1]):
                    low += 1
                    continue
                if (sum == 0):
                    arr.append([nums[index], nums[low], nums[high]])
                    low += 1
                elif (sum > 0):
                    high -= 1
                else:
                    low += 1
            index += 1
        return arr