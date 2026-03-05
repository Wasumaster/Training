class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        res = []
        complement = 0
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                res.append(i)
                res.append(d[complement])
                return res
            else:
                d[nums[i]] = i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        