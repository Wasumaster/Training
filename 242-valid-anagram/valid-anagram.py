class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = []
        tl = []
        if len(s) != len(t):
            return False


        return sorted(s) == sorted(t)
        