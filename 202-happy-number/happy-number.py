class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        been = set()

        while number != 1:
            
            if number in been:
                return False
            been.add(number)
            
            new_sum = 0
            current_num = number 

            while current_num > 0:
                d = current_num % 10
                new_sum += d * d
                current_num = current_num // 10
            number = new_sum
        return True

       