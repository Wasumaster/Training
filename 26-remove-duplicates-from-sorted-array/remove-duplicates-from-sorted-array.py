class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] in d:
                continue
            else:
                count += 1
                if nums[i] in d:
                    d[nums[i]] += 1
                else:
                    d[nums[i]] = 1
                
                nums[k] = nums[i]

                k += 1 
        return count