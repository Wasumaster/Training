class Solution(object):
    def fizzBuzz(self, n):
        outputlist = []
        for i in range(n):
            i = i + 1
            if i % 3 == 0 and i % 5 ==0:
                outputlist.append("FizzBuzz")
                continue
            if i % 3 == 0:
                outputlist.append("Fizz")
                continue
            if i % 5 == 0:
                outputlist.append("Buzz")
                continue
            string_num = "{}".format(i) 
            outputlist.append(string_num)
            
        return outputlist
        """
        :type n: int
        :rtype: List[str]
        """
        