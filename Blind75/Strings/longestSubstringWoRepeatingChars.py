# Given a string s, find the length of the longest substring without repeating characters.
# Time complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        index = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[index])
                index += 1
            charSet.add(s[r])
            res = max(res, r - index + 1)
        return res