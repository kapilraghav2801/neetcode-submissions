class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans

        """ TC: O(n) and SC: O(1)"""
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # for num in nums:
        #     if freq[num] == 1:
        #         return num

        """TC: O(n) and SC: O(n)"""
        # for num in nums:
        #     count = 0

        #     for x in nums:
        #         if x == num:
        #             count += 1

        #     if count == 1:
        #         return num

        """TC: O(n2), SC: O(1)"""



# ==========================================
# Companies Asking This Question (Frequency)
# ==========================================
# 
# [0 - 3 months]
# - Bloomberg: 6
# - Google: 4
# - Microsoft: 4
# - Amazon: 4
# - Meta: 2
# 
# [0 - 6 months]
# - TCS: 3
# 
# [6 months ago]
# - Adobe: 2
# - Cisco: 2
# - Accenture: 2
# - Cognizant: 2
# ==========================================
        