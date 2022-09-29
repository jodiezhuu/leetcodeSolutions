# You are given an integer array `height` of length `n`. There 
# are `n` vertical lines drawn such that the two endpoints of the 
# `ith` line are `(i, 0)` and `(i, height[i])`.

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return *the maximum amount of water a container can store*.

# **Notice** that you may not slant the container.

# Time Complexity: O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while (right > left):
            width = right - left
            length = min(height[left], height[right])
            curr_area = length * width
            if curr_area > max_area:
                max_area = curr_area
            if (height[left] < height[right]):
                left += 1
            elif (height[right] < height[left]):
                right -= 1
            else:
                left += 1
        return max_area