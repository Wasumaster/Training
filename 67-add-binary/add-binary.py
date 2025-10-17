class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a , 2)
        decimal_b = int(b , 2)
        res = decimal_a + decimal_b
        bin_l = bin(res)[2:]
        return bin_l