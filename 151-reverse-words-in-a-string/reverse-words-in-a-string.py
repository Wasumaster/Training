class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        list_s = s.split()
        reverse_list = list_s[::-1]
        return " ".join(reverse_list)