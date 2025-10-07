class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        value = 0
        max_cur = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    value = (nums[i]-1)*(nums[j]-1)
                    if value > max_cur:
                        max_cur = value
        return max_cur

