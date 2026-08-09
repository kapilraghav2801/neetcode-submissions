class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # Did we find the target?
            if nums[mid] == target:
                return mid
                
            # Check if the LEFT half is perfectly sorted
            if nums[start] <= nums[mid]:
                # Does the target fall within the boundaries of this sorted left half?
                if nums[start] <= target < nums[mid]:
                    # It's in the left half! Discard the right.
                    end = mid - 1
                else:
                    # It's NOT in the left half! Discard the left.
                    start = mid + 1
                    
            # Otherwise, the RIGHT half must be perfectly sorted
            else:
                # Does the target fall within the boundaries of this sorted right half?
                if nums[mid] < target <= nums[end]:
                    # It's in the right half! Discard the left.
                    start = mid + 1
                else:
                    # It's NOT in the right half! Discard the right.
                    end = mid - 1
                    
        return -1






        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i

        # return -1
        


# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Amazon: 18
# - Google: 13
# - Meta: 7
# - Bloomberg: 7
# - Microsoft: 5
# - Oracle: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - LinkedIn: 3
# - TikTok: 3
# - Goldman Sachs: 3
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Grammarly: 15
# - Walmart Labs: 13
# - Nvidia: 9
# - TCS: 7
# - Apple: 6
# - Yandex: 6
# - Zoho: 5
# - Autodesk: 5
# - PayPal: 5
# - NewsBreak: 5
# =================================================