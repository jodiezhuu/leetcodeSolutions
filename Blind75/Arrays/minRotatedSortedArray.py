# Suppose an array of length `n` sorted in ascending order is **rotated** 
# between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

    # `[4,5,6,7,0,1,2]` if it was rotated `4` times.
    # `[0,1,2,4,5,6,7]` if it was rotated `7` times.

# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the 
# array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element 
# of this array*

# You must write an algorithm that runs in `O(log n) time.`

# Time Complexity: O(log n)
class Solution:

    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        curr_min = nums[0]
        if nums[low] > nums[high]: ## array is rotated
            curr_min = nums[high]
            while (high > low):
                mid = (low + high) // 2
                if nums[mid] < curr_min:
                    curr_min = nums[mid]  
                if (nums[mid] > nums[low]):
                    low = mid
                else:
                    high = mid   
        return curr_min