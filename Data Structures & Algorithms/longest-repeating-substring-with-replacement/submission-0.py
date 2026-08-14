class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        max_len = 0
        max_freq = 0
        freq = {}

        for j in range(n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])

            while (j-i+1) - max_freq > k:
                freq[s[i]] -= 1
                i += 1

            max_len = max(max_len, j-i+1)

        return max_len
        # n = len(s)
        
        # for i in range(n):
        #     freq = {}
        #     max_len = 0
        #     for j in range(i,n):

        #         freq[s[j]] = freq.get(s[j], 0) + 1
        #         max_freq = max(freq.values())

        #         if (j-i+1) - max_freq <= k:
        #             max_len = max(max_len, j-i+1)

        #     return max_len



        



# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 10
# - Amazon: 5
# - Microsoft: 3
# - Bloomberg: 3
# - DE Shaw: 3
# - Infosys: 2
# - Zoho: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Meta: 3
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Goldman Sachs: 6
# - Yandex: 5
# - ServiceNow: 4
# - CRED: 3
# - Adobe: 2
# - ByteDance: 2
# - Zepto: 2
# - Docusign: 2
# - UiPath: 2
# =================================================