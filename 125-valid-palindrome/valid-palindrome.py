class Solution:
    def isPalindrome(self, s: str) -> bool:
        napis = s.replace(" ", "")

        l = 0
        r = len(napis) - 1
        
        while l < r:

            if not napis[r].isalnum():
                r -= 1
                continue
                
            if not napis[l].isalnum():
                l += 1
                continue
                
            if napis[r].lower() == napis[l].lower():
                r -= 1
                l += 1
            else:
                return False
                
        return True
