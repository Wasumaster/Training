class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''
        for n in digits:
            st += str(n)
        print(st)
        si = int(st)
        si += 1
        ss = str(si)
        res = []
        for ch in ss:
            ci = int(ch)
            res.append(ci)
        return res