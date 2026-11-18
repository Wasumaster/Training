class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = {"]": "[", "}":"{", ")":"("}
        for paranthesis in s:

            if len(stack) > 0 and paranthesis in closed_to_open:
                if stack[-1] == closed_to_open[paranthesis]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paranthesis)
        if len(stack) > 0:
            return False
        else:
            return True