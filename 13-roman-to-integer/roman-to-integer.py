class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        d = {'I'  : 1,
        'V' :5,
        'X' :10,
        'L' :50,
        'C' :100,
        'D' :500,
        'M' :1000
        }
        p = 0
        while p < len(s):
            if p + 1 < len(s):
                if d[s[p + 1]] > d[s[p]]:
                    res +=  d[s[p + 1]] - d[s[p]]
                    p += 2
                else:
                    res +=  d[s[p]]
                    p += 1
            else:
                res +=  d[s[p]]
                p += 1
        return res