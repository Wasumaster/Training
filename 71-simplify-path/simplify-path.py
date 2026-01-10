class Solution:
    def simplifyPath(self, path: str) -> str:
        pathTable = path.split("/")
        stack = []
        for element in pathTable:
            if element == "." or element == '':
                continue
            if element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)

        output = '/'
        len_stack = len(stack)
        for i in range(len_stack):
            output += stack[i]
            if i != len_stack - 1:
                output += "/"
        return output
