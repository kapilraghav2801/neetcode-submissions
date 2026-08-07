class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_water = 0

        while left < right:
            width = right - left

            curr_height = min(height[right], height[left])

            curr_water = width * curr_height

            if curr_water > max_water:
                max_water = curr_water

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1

        return max_water


        # max_water = 0
        # n = len(height)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         width = j - i
        #         curr_height = min(height[i], height[j])

        #         curr_water = width * curr_height

        #         if curr_water > max_water:
        #             max_water = curr_water

        # return max_water

# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 22
# - Amazon: 17
# - TCS: 15
# - Microsoft: 10
# - Bloomberg: 10
# - Meta: 5
# - Infosys: 4
# - Goldman Sachs: 3
# 
# [0 - 6 months -- FEB - JULY 2026]
# - IBM: 2
# - Walmart Labs: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Oracle: 12
# - Flipkart: 9
# - Zoho: 9
# - TikTok: 8
# - Yandex: 7
# - SAP: 7
# - Apple: 6
# - Nvidia: 6
# - Capital One: 5
# - Deloitte: 4
# =================================================

        