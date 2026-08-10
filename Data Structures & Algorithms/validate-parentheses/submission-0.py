class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {')':'(' ,'}':'{', ']':'[' }


        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

            else:
                stack.append(ch)

        return not stack
         
# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 20
# - Meta: 9
# - Amazon: 9
# - Bloomberg: 8
# - BlackRock: 6
# - Microsoft: 4
# - TCS: 3
# - Intuit: 3
# - Accolite: 2
# - Virtu Financial: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - LinkedIn: 8
# - IBM: 7
# - Tripadvisor: 4
# - Criteo: 2
# - Epic Systems: 2
# - Autodesk: 2
# - Odoo: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Apple: 26
# - Oracle: 20
# - Zoho: 15
# - Walmart Labs: 14
# - TikTok: 13
# - Infosys: 12
# - Yandex: 12
# - Nvidia: 11
# =================================================
        