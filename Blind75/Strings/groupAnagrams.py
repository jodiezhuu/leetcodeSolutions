# Given an array of strings `strs`, group **the anagrams** together. 
# You can return the answer in **any order**.

# An **Anagram** is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original letters exactly once.

# Time complexity: O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 ## index a to z
            for c in s:
                count[ord(c) - ord("a")] += 1 ## ord returns the integer value of the char
            res[tuple(count)].append(s) ## use tuples because hashable, arrays arent
        return res.values()