class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            actual = (i + 1) * [1]
            for j in range(1, i):
                prev = result[i-1]
                left  = prev[j-1]
                right = prev[j]

                actual[j] = left + right
            result.append(actual)
        return result


