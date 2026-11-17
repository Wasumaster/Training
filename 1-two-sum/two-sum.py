class Solution(object):
    def twoSum(self, nums, target):
       slownik = {}
       suplement = 0
       for i in range(len(nums)):
        suplement = target - nums[i]
        if suplement in slownik:
            return [i, slownik[suplement]]
        else:
            slownik[nums[i]] = i            

       
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        