class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictransom = {}
        dictmag = {}
        for s in ransomNote:
            if s in dictransom:
                dictransom[s] += 1
            else:
                dictransom[s] = 1

        for s in magazine:
            if s in dictmag:
                dictmag[s] += 1
            else:
                dictmag[s] = 1
        for litera, ilosc_potrzebna in dictransom.items():

            ilosc_dostepna = dictmag.get(litera, 0)

            if ilosc_dostepna < ilosc_potrzebna:
                return False
        return True