class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            # FIX 1: Safely calculate the middle index
            mid = start + (end - start) // 2
            
            if target == nums[mid]:
                return mid
                
            # FIX 2: Compare the VALUE at mid, not the index itself
            elif nums[mid] < target:
                # The target is larger, search the right half
                start = mid + 1
                
            else:
                # The target is smaller, search the left half
                end = mid - 1
                
        return -1

# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 12
# - Amazon: 5
# - Meta: 3
# - Microsoft: 3
# - Bloomberg: 3
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Infosys: 4
# - TCS: 2
# - Oracle: 2
# - Pure Storage: 2
# - Yandex: 2
# - Cognizant: 2
# =================================================
        