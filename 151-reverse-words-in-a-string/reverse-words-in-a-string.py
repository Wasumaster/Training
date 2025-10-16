class Solution:
    def reverseWords(self, s: str) -> str:
        slowa = s.split()
        reverse = slowa[::-1]
        separator = ' '
        final = separator.join(reverse)
        return final