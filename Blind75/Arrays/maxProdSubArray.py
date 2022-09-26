# Given an integer array numsfind a contiguous non-empty subarray within the 
# array that has the largest product, and return the product.

# Time complexity: O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max = [nums[0]]
        local_min = [nums[0]]
        curr_prod = 1
        for i in range(1, len(nums)):
            ## append local max and min elements into array
                local_max.append(max(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))
                local_min.append(min(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))
        return max(local_max)