class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = {"]": "[", "}":"{", ")":"("}
        for bracekt in s:
            if bracekt == '(' or bracekt == "{" or bracekt == "[":
                stack.append(bracekt)
            else:
                if stack and stack[-1] == closed_to_open[bracekt]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
