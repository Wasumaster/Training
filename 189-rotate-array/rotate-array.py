class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  
        split = n - k

        nums[:] = nums[split:] + nums[:split]