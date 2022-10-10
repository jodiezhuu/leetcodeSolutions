# Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, 
# determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Time Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            else:
                if len(stack) == 0: ## len is o(1) in python
                    return False
                closingBracket = stack.pop()
                if c != closingBracket:
                    return False
        if len(stack) != 0:
            return False
        return True