class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        dl = len(nums)
        k = k % dl
        t_arr = [0] * dl
        last_nums = nums[dl - k:]
        first_nums = nums[:dl-k]
        arr = last_nums[:] + first_nums[:]
        nums[:] = arr
        