class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        window = set()
        for i in range(n):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])

        return False

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i] == nums[j] and abs(i-j) <= k:
#                     return True

#         return False
        

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         seen = {}

#         for i,num in enumerate(nums):
#             if num in seen and i - seen[num] <= k:
#                 return True
#             seen[num] = i
#         return False
        


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