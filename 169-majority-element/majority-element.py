class Solution(object):
    def majorityElement(self, nums):
        d = {}

        for number in nums:
            if number in d:
                d[number] += 1
            else:
                d[number] = 0
        major_element = max(d.values())

        for key in d:
            if d[key] == major_element:
                return key

    
        """
        :type nums: List[int]
        :rtype: int
        """
        