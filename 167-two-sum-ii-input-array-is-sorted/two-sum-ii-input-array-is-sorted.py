class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_front = 0
        pointer_back = len(numbers) - 1
        while pointer_front < pointer_back:
            if numbers[pointer_front] + numbers[pointer_back] == target:
                return [pointer_front + 1, pointer_back + 1]
                break
            else: 
                if numbers[pointer_front] + numbers[pointer_back] > target:
                    pointer_back -= 1
                else:
                    pointer_front += 1
