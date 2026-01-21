class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        mv = k % len(nums)
        dl = len(nums) - mv 
        right = nums[:dl]
        left = nums[dl:]
        combined = left + right
        nums[:] = combined
