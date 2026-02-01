class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[k] = nums[i]
                k += 1
                count += 1
        return count
