class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dl = 0
        s = s.strip()
        k = len(s) -1
        while k >= 0:
            if s[k].isalpha():
                dl += 1
            elif s[k] == ' ':
                break
            k -= 1
        return dl