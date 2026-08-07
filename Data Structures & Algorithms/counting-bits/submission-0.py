class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        for i in range(1,n+1):
            result[i] = result[i>>1] + (i&1)
        return result
        # result = [0] * (n+1)
        # for i in range(1,n+1):
        #     if i % 2 == 0:
        #         result[i] = result[i//2]
        #     else:
        #         result[i] = result[i//2] + 1

        # return result

        
        # result = []

        # for i in range(n+1):
        #     result.append(bin(i).count('1'))

        # return result



# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Amazon: 3
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Google: 13
# - Microsoft: 9
# - Meta: 8
# - Bloomberg: 4
# - Nvidia: 3
# - Apple: 2
# - Oracle: 2
# =================================================
        
        