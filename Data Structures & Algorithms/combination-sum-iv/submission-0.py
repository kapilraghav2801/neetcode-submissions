class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """ we can think about backtracking when question is saying something like all possible/combination/subsets
        and for BT 1. do something 2. Explore 3. Revert step1 and further explore"""
        memo = {}

        def solve(i,t):
            if t == 0:
                return 1

            if t < 0 or i == len(nums):
                return 0

            if (i,t) in memo:
                return memo[(i,t)]

            take = solve(0, t- nums[i])
            skip = solve(i+1, t)

            memo[(i,t)] = take + skip 

            return memo[(i,t)]

        return solve(0, target)
        # memo = {}
        # def solve(current_target):
        #     if current_target == 0:
        #         return 1
        #     if current_target < 0:
        #         return 0

        #     if current_target in memo:
        #         return memo[current_target]

        #     res = 0

        #     for num in nums:
        #         res += solve(current_target - num)

        #     memo[current_target] = res

        #     return res

        # return solve(target)


        



# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Google: 2
# - Amazon: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Meta: 4
# - Bloomberg: 3
# - Microsoft: 2
# - TikTok: 2
# =================================================