class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_front = 0
        pointer_back = len(numbers) - 1
        res = False
        arr = []
        while pointer_front < pointer_back and res == False:
            if numbers[pointer_front] + numbers[pointer_back] == target:
                pointer_front += 1
                pointer_back += 1
                arr.append(pointer_front)
                arr.append(pointer_back)
                return arr
                break
            else: 
                if numbers[pointer_front] + numbers[pointer_back] > target:
                    pointer_back -= 1
                else:
                    pointer_front += 1
