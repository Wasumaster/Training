class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                c += 1
                j += 1
            
        return c
            
