class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dl = 0
        s = s.strip()
        i = len(s) - 1 
        while s[i].isalpha() and i >= 0:
            dl += 1
            i -= 1
        return dl 