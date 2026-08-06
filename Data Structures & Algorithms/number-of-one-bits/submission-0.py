class Solution:
    def hammingWeight(self, n: int) -> int:
        """Brian Kern"""
        # count = 0
        # while n != 0:
        #     count += 1

        #     n = n & (n-1)

        # return count

        """Check each bit"""

        # count = 0
        # for i in range(32):
        #     if (n >> i) & 1:
        #         count += 1

        # return count 

        """Bit manipulation"""
        # count = 0
        # while n:
        #     count += n % 2 #module count if remainder is 1 else 0
        #     n //= 2

        # return count

        """App-4 : inbuilt python"""
        return n.bit_count()






# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Meta: 2
# - Amazon: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Box: 7
# - Microsoft: 5
# - Bloomberg: 4
# - Apple: 4
# - Verkada: 3
# - Nvidia: 2
# =================================================
        