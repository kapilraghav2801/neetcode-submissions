class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1


        while start < end:
            mid = start + (end- start) // 2

            if nums[mid] > nums[end]:
                start = mid + 1

            else:
                end = mid

        return nums[start]
        # curr_min = nums[0]

        # for num in nums:
        #     if num < curr_min:
        #         curr_min = num


        # return curr_min

        


# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Amazon: 6
# - Google: 4
# - Meta: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Bloomberg: 4
# - TCS: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Microsoft: 21
# - Goldman Sachs: 13
# - TikTok: 6
# - Apple: 3
# - Oracle: 3
# - Walmart Labs: 3
# - Uber: 3
# - Yandex: 3
# - IBM: 2
# - Infosys: 2
# =================================================