class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      pointer1 = 0
      suma = 1 
      for i in range(len(nums)):
        if nums[i] != val:
            nums[pointer1] = nums[i]
            pointer1 += 1
            
            suma += 1
      return suma - 1 
            

            
