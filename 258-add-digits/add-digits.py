class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        n = num 
        while n > 9:
            s = 0
            temp = n
            while temp > 0:
                c = temp % 10
                s += c
                temp = temp  // 10
            n = s
        return n