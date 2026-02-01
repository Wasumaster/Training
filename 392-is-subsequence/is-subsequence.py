class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dlugosc_s = len(s)
        pointer_s = 0
        if dlugosc_s == 0:
            return True
        for i in range(len(t)):
            if  s[pointer_s] == t[i]:
                pointer_s += 1
 
                if pointer_s == dlugosc_s:
                    return True
        return False

                        