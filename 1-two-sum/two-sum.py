class Solution(object):
    def twoSum(self, nums, target):
       slownik = {}
       suplement = 0
       for i in range(len(nums)):
        suplement = target - nums[i]

        if suplement in slownik:
            arr = []
            arr.append(i)
            arr.append(slownik[suplement])
            return arr
        else:
            slownik[nums[i]] = i            

       
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        