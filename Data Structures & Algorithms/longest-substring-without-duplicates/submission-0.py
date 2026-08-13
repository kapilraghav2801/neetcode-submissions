class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s) 
        # max_len = 0      
        # for i in range(n):
        #     seen = {} 
        #     for j in range(i,n):
        #         if s[j] not in seen:
        #             seen[s[j]] = seen.get(s[j], 0) + 1
        #             max_len = max(max_len, j-i+1)

        #         else:
        #             break

        # return max_len

        # n = len(s)
        # i = 0
        # j = 0
        # seen = {}
        # max_len = 0

        # for j in range(n):
        #     seen[s[j]] = seen.get(s[j], 0) + 1

        #     while seen[s[j]] > 1:
        #         seen[s[i]] -= 1

        #         if seen[s[i]] == 0:
        #             del seen[s[i]]

        #         i += 1

        #     max_len = max(max_len, j - i + 1)

        # return max_len

        seen = {}
        i = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)

            seen[s[j]] = j
            max_len = max(max_len, j - i + 1)

        return max_len

        


# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Amazon: 40
# - Google: 37
# - Bloomberg: 14
# - Meta: 12
# - Microsoft: 10
# - TCS: 5
# - Infosys: 4
# - Deloitte: 3
# - Goldman Sachs: 3
# - Cognizant: 3
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Spotify: 7
# - Apple: 4
# - Zoho: 4
# - JPMorgan Chase: 3
# - EPAM Systems: 3
# - Visa: 3
# - Netflix: 3
# - Yandex: 3
# - Qualcomm: 3
# - IBM: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Oracle: 36
# - TikTok: 34
# - Walmart Labs: 17
# - Nvidia: 17
# - Turing: 15
# - Salesforce: 11
# - Cisco: 10
# - ServiceNow: 10
# - Accenture: 9
# - PayPal: 6
# =================================================
        