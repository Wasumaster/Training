class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictransom = {}
        dictmag = {}
        for c in ransomNote:
            if c in dictransom:
                dictransom[c] += 1
            else:
                dictransom[c] = 1
        
        for c in magazine:
            if c in dictmag:
                dictmag[c] += 1
            else:
                dictmag[c] = 1
        for key in dictransom:
            if key in dictmag and dictmag[key] >= dictransom[key] :
                continue
            else:
                return False
        return True 