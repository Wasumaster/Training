class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        dl = len(nums)
        k = k % dl
        arr = nums[dl - k:] + nums[:dl - k]
        nums[:] = arr
        