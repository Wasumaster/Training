class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dl = len(nums)
        left = dl * [0]
        right = dl * [0]
        ilo1 = 1
        ilo2 = 1
        for i in range(dl):
            if i > 0:
                ilo1 = ilo1 * nums[i - 1]
                left[i] = ilo1
            else:
                left[0] = 1

        for j in range(dl -1, -1 ,-1):
            if j == dl -1 :
                right[dl -1] = left[j]
            else:
                ilo2 = ilo2 * nums[j + 1]
                right[j] = ilo2 * left[j]
        return right




        dl = len(nums)
        f_list = dl * [0]
        for i in range(len(nums)):
            w = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    w = w * nums[j]

            f_list[i] = w
        return f_list
                