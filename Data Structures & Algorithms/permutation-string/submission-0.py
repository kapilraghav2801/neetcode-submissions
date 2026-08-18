
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        for i in range(m-n+1):
            window = s2[i:i+n]

            if sorted(window) == sorted(s1):
                return True

        return False

        





# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Meta: 5
# - Amazon: 5
# - Bloomberg: 3
# - Google: 2
# - Microsoft: 2
# - TCS: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Apple: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Yandex: 16
# - Oracle: 4
# - Walmart Labs: 4
# - Databricks: 4
# - TikTok: 3
# - Cisco: 2
# =================================================