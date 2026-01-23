class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        c_pre = strs[0]
        for i in range(1, len(strs)): 
            if len(strs[i]) < len(c_pre):
                c_pre = c_pre[:len(strs[i])]
            dl = min(len(c_pre), len(strs[i]))
            for j in range(dl):
                if j < len(c_pre) and c_pre[j] == strs[i][j]:
                    continue
                else:
                    c_pre = c_pre[:j]
                    break
        return c_pre

            
