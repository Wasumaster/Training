class Solution:
    def fib(self, n: int) -> int:
        c1 = 0
        c2 = 1
        suma = 0
        for _ in range(n):
            suma = c1 + c2
            c2 = c1
            c1 = suma

        return suma