class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:]
        padded_str = binary_str.zfill(32)
        flipped_str = padded_str[::-1]
        result = int(flipped_str, 2)
    
        return result