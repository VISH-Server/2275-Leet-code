class Solution:
    def largestCombination(self, candidates):
        # We assume integers up to 10^7, so we need up to 24 bits.
        # Initializing a list to count set bits at each position
        bit_count = [0] * 24

        for num in candidates:
            # Check each bit position
            for i in range(24):
                # Check if the i-th bit is set in num
                if num & (1 << i):
                    bit_count[i] += 1

        # The answer is the maximum count in bit_count array
        return max(bit_count)
