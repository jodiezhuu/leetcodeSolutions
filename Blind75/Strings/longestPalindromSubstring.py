# Given a string s, return the longest palindromic substring in s.

# A string is called a palindrome string if the reverse of that string 
# is the same as the original string.

# Time complexity: O(m * n), m is the length of the string, n is the length of the longest palindrome
class Solution:
    def longestPalindrome(self, s: str) -> str:
        currLongest = ""
        longestLength = 0
        for i in range(len(s)):
            left, right = i, i
            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                if (right - left + 1) > longestLength:
                    currLongest = s[left:right + 1] ## note: right is not inclusive 
                    longestLength = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                if (right - left + 1) > longestLength:
                    currLongest = s[left:right + 1]
                    longestLength = right - left + 1
                left -= 1
                right += 1
                
        return currLongest