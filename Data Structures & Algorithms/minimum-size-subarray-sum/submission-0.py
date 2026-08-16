class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        curr_sum = 0
        min_len = float('inf')

        for j in range(n):
            curr_sum += nums[j]

            while curr_sum >= target:
                min_len = min(min_len, j-i+1)

                curr_sum -= nums[i]
                i += 1

        return 0 if min_len == float('inf') else min_len
        # n = len(nums)
        # min_len = float('inf')

        # for i in range(n):
        #     current_sum = 0
        #     for j in range(i,n):
        #         current_sum += nums[j]

        #         if current_sum >= target:
        #             min_len = min(min_len, j-i+1)
        #             break

                

        # if min_len == float('inf'):
        #     return 0

        # return min_len


        



# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 10
# - Meta: 8
# - Microsoft: 3
# - Amazon: 3
# - Bloomberg: 3
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - BCG: 8
# - DoorDash: 7
# - TikTok: 6
# - Goldman Sachs: 4
# - Oracle: 3
# - TCS: 2
# - Apple: 2
# - DE Shaw: 2
# - Nvidia: 2
# - Yandex: 2
# =================================================