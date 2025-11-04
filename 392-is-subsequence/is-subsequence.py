class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_t = 0
        pointer_s = 0
        suma = 0
        dl_s = len(s)
        dl = len(t)
        if dl_s == 0 and dl > 0:
            return True

        while pointer_t < dl and pointer_s < dl_s:
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
                pointer_t += 1
                suma += 1
            else: 
                pointer_t += 1
        if suma == dl_s:
            return True
        else:
            return False