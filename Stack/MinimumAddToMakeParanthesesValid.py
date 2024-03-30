class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(0, len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
