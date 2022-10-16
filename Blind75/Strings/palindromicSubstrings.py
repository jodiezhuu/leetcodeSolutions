# Given a string `s`, return *the number of **palindromic substrings** in it*.

# A string is a **palindrome** when it reads the same backward as forward.

# A **substring** is a contiguous sequence of characters within the string.

# Time Complexity: O(n*m) where n is length of string, m is length of longest palindrome
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        ## for odd number
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        ## for even number
        for i in range(len(s)):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res