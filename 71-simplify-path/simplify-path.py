class Solution:
    def simplifyPath(self, path: str) -> str:
        pathTable = path.split("/")
        stack = []
        for element in pathTable:
            if element == "." or element == '':
                continue
            elif element == '..':
                if stack: 
                    stack.pop()
            else:
                stack.append(element)
        return '/'+ '/'.join(stack)


        