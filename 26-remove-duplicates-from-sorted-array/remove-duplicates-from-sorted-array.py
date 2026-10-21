class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index1 = 0
        for i in range(1,len(nums)):
            if nums[index1] != nums[i]:
                index1 += 1
                nums[index1] = nums[i]
                
        return index1 + 1
