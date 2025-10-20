class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:]
        padded_str = binary_str.zfill(32)
        flipped_str = padded_str[::-1]
        result = int(flipped_str, 2)
    
        return result
        """
        res = 0
        for i in range(32):
            last_bit = n & 1
            res = res << 1
            res = res | last_bit

            n = n >> 1
        return res
        """