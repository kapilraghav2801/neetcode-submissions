class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n <= 2:
            return n
        a,b = 1, 2

        for _ in range(3, n+1):
            a, b = b, a+b

        return b
        # """Bottom-up"""
        # if n <= 2:
        #     return n

        # dp = [0] * (n+1)

        # dp[1], dp[2] = 1,2

        # for i in range(3, n+1):
        #     dp[i]= dp[i-1] + dp[i-2]

        # return dp[n]
        # if n < 0:
        #     return 0

        # if n == 0:
        #     return 1

        # if n in memo:
        #     return memo[n]

        # memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)

        # return memo[n]
        



# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 15
# - Amazon: 11
# - Bloomberg: 7
# - Microsoft: 5
# - Meta: 4
# - Infosys: 3
# - TCS: 2
# - Intuit: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Deloitte: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Accenture: 12
# - Grammarly: 12
# - Zoho: 11
# - TikTok: 7
# - IBM: 4
# - Apple: 4
# - Goldman Sachs: 4
# - Oracle: 3
# - Nvidia: 3
# - Cognizant: 3
# =================================================