class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for paren in s:
            if paren in m:
                stack.append(paren)
            else:
                if not stack or m[stack.pop()] != paren:
                    return False

        if stack:
            return False

        return True
