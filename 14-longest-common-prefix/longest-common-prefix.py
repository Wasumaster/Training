class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        c_p = ''
        i_len = 0
        if len(strs) >= 2:
            if len(strs[0]) >= len(strs[1]):
                i_len = len(strs[1])
            else:
                i_len = len(strs[0])

            for i in range(i_len):
                if strs[0][i] == strs[1][i]:
                    c_p += strs[1][i]
                else:
                    break
            if len(strs) == 2:
                return c_p
            common_prefix = c_p

        for i in range(1, len(strs)):
            if strs[i] == '':
                return ''
                break
            cp = ''
            it_len = 0
            if len(common_prefix) >= len(strs[i]):
                it_len = len(strs[i])
            else:
                it_len = len(common_prefix)
            for j in range(it_len):
                if strs[i][j] == common_prefix[j]:
                    cp += strs[i][j]
                    continue
                else:
                    common_prefix = cp
                    break
            common_prefix = cp
        return common_prefix

