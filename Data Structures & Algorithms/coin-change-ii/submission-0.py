class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # 0 amount banane ka 1 tarika
        
        # OUTER LOOP: Coins (To avoid permutations)
        for coin in coins:
            # INNER LOOP: Amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]



# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 3
# - Amazon: 3
# - Microsoft: 2
# - Infosys: 2
# - Mastercard: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Meta: 8
# - Bloomberg: 5
# - TikTok: 3
# - DE Shaw: 2
# - Pornhub: 2
# =================================================