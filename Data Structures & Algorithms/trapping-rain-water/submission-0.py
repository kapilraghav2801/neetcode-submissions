class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        total_water = 0

        while left < right:

            if height[left] <= height[right]:

                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    total_water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]

                else:
                    total_water += right_max - height[right]

                right -= 1


        return total_water

# class Solution:
#     def trap(self, height: list[int]) -> int:
#         if not height: return 0
        
#         n = len(height)
#         left_max = [0] * n
#         right_max = [0] * n
        
#         # Precompute the highest wall to the left of every index
#         left_max[0] = height[0]
#         for i in range(1, n):
#             left_max[i] = max(left_max[i - 1], height[i])
            
#         # Precompute the highest wall to the right of every index
#         right_max[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             right_max[i] = max(right_max[i + 1], height[i])
            
#         total_water = 0
#         # Apply our physics formula
#         for i in range(n):
#             total_water += min(left_max[i], right_max[i]) - height[i]
            
#         return total_water

# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Amazon: 43
# - Google: 37
# - Goldman Sachs: 12
# - Bloomberg: 11
# - Meta: 6
# - Microsoft: 6
# - Snowflake: 4
# - TCS: 3
# - Infosys: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Oracle: 2
# - Walmart Labs: 2
# - Nvidia: 2
# - Docusign: 2
# - Qualcomm: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - TikTok: 29
# - Zoho: 14
# - Zopsmart: 13
# - Yandex: 12
# =================================================

        