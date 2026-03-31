class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
                c += 1
        return c 
            
