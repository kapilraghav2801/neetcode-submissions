class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1


        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


        # # Step 1: Filter out non-alphanumeric characters and convert to lowercase
        # cleaned = [char.lower() for char in s if char.isalnum()]
        
        # # Step 2: Compare the list to its reversed version
        # return cleaned == cleaned[::-1]


# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 11
# - Bloomberg: 11
# - Amazon: 9
# - Meta: 6
# - Microsoft: 2
# - Infosys: 2
# - TCS: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Apple: 4
# - Deloitte: 2
# - Cognizant: 2
# - Axon: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Yandex: 19
# - BCG: 11
# - CleverTap: 11
# - Oracle: 6
# - Comcast: 3
# - TikTok: 3
# - Zoho: 3
# - Cisco: 3
# - Intuit: 3
# - SAP: 3
# =================================================