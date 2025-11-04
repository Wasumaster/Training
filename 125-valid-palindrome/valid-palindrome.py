class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for c in s:
            if c.isalpha() == True:
                s1 += c.lower()
            if c.isdigit() == True:
                s1 += c
        if s1 == s1[::-1]:
            return True
        else:
            return False