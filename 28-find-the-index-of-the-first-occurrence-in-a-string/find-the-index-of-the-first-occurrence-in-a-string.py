class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        dl = len(needle)
        for i in range(len(haystack)):
            c = 0
            p = 0 
            for j in range(dl):
                if i + j < len(haystack):
                    if haystack[i + j] == needle[j]:
                        c += 1
                        p = j
                    else:
                        c = 0
                        break
            if c == dl:
                return i
                break
        return res 