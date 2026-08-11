class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float('inf')

        for price in prices:
            min_profit = min(min_profit, price)
            max_profit = max(max_profit, price - min_profit)

        return max_profit

        # n = len(prices)
        # max_profit = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        #         # if profit > max_profit:
        #         #     max_profit = profit


        # return max_profit


# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Amazon: 40
# - Google: 31
# - Bloomberg: 12
# - Meta: 9
# - Microsoft: 8
# - TCS: 4
# - Infosys: 3
# - Apple: 3
# - Atlassian: 3
# - Media.net: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - IBM: 3
# - Goldman Sachs: 3
# - JPMorgan Chase: 2
# - Adobe: 2
# - Walmart Labs: 2
# - TikTok: 2
# - Nvidia: 2
# - Accenture: 2
# - Mastercard: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Uber: 17
# - Zoho: 16
# - Agoda: 15
# - Morgan Stanley: 14
# - Visa: 12
# - Zoox: 12
# - Citadel: 11
# - Oracle: 9
# - Tesla: 8
# - Deloitte: 6
# =================================================


        