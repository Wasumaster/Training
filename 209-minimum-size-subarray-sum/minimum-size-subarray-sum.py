class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - left +1)
                total -= nums[left]
                left += 1
        if res == float("inf"):
            return 0
        else:
            return res 















