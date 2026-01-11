class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        pointer1 = 0
        pointer2 = 0
        len_nums = len(nums)
        if len_nums == 0:
            return output
        while pointer1 < len_nums or pointer2 <0:
            pointer2 = pointer1 + 1
            iterator = 1
            while pointer2 < len_nums and pointer1 - 1 < len_nums and nums[pointer1] + iterator == nums[pointer2]:
                pointer2 += 1
                iterator += 1
            if pointer2 == pointer1 + 1:
                output.append(str(nums[pointer1]))
            else:
                output.append(str(nums[pointer1]) + "->" + str(nums[pointer2 - 1 ]))
            pointer1 = pointer2
        return output
                