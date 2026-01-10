class Solution(object):
    def twoSum(self, nums, target):
        output = []
        arr = []
        cal = 0
        for i in range(len(nums)):
            if nums[i] in arr:
                output.append(i)
                output.append(arr.index(nums[i]))
                break

            cal = target - nums[i]
            arr.append(cal)
              
        return output
        """
    

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        