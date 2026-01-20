class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointers(one go-through arrey, secend keep track on output arrey)
        #crerreate a hash map to check weather num is already in
        #if yes we check if one of if twice , if not update 
        #[1,2,3,444,55,666]

        been = {}
        i = 0 # output_arrey_pointer
        been[nums[i]] = 1
        for j in range(1, len(nums)):
            if nums[j] in been:
                if been[nums[j]] > 1:
                    continue
                else:
                    i += 1
                    nums[i] = nums[j]
                    been[nums[j]] += 1
            else:
                been[nums[j]] = 1
                i += 1
                nums[i] = nums[j]
        return i + 1