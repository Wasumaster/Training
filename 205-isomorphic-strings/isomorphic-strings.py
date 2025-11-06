class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if (c1 in dic_s and dic_s[c1] != c2) or (c2 in dic_t and dic_t[c2] != c1):
                return False
            dic_s[c1] = c2
            dic_t[c2] = c1 
        return True

