class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        c_pre = ''
        for i in range(len(strs[0])):
            for letter in strs:
                if i == len(letter) or letter[i] != strs[0][i]:
                    return c_pre
            c_pre += strs[0][i]

        return c_pre