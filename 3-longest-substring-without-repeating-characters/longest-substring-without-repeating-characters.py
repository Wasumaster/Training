class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[r])
            cur_length = r - left +1
            maxLength = max(maxLength, cur_length)
        return maxLength

        

     