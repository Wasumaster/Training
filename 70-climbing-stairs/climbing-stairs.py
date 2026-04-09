class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        last_res1 = 1
        last_res2 = 2
        suma = 0
        for i in range(2,n):
            suma = last_res1 + last_res2
            last_res1 = last_res2
            last_res2 = suma
        
        return suma
