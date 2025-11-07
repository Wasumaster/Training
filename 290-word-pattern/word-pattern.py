class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: 
        slowa_to_char = {}
        char_to_slowa = {}
        slowa = s.split()
        if len(slowa) != len(pattern):
            return False

        for char, word in zip(pattern, slowa):
            if char in char_to_slowa:
                if char_to_slowa[char] != word:
                    return False
            else:
                if word in slowa_to_char:
                    if slowa_to_char[word] != char:
                        return False
            char_to_slowa[char] = word
            slowa_to_char[word] = char
        return True