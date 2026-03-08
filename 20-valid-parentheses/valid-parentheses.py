class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(",
            "]": "[",
            "}": "{" }

        for p in s:
            if p in close_to_open:
                if len(stack) > 0 and close_to_open[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        if len(stack) == 0:
            return True
        else:
            return False