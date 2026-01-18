class Solution:
    def isHappy(self, n: int) -> bool:
        been = set()
        number  = n
        while number != 1:

            if number in been:
                return False
            else:
                been.add(number)
            suma = 0
            while number > 0:
                d = number % 10
                suma += d * d
                number = number // 10

            number  = suma
        return True 