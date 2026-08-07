class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}

        # for i, num in enumerate(numbers):
        #     compliment = target - num

        #     if compliment in seen:
        #         return [seen[compliment] + 1, i + 1]
            
        #     seen[num] = i


        left = 0
        right = len(numbers) - 1

        while left < right:

            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]

            elif curr_sum < target:
                left += 1

            else:
                right -= 1



    #     class Solution:
    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
    #     n = len(numbers)
        
    #     # Iterate through every number as our "first" number
    #     for i in range(n):
    #         complement = target - numbers[i]
            
    #         # Binary search for the complement in the REST of the array
    #         left = i + 1
    #         right = n - 1
            
    #         while left <= right:
    #             mid = left + (right - left) // 2
                
    #             if numbers[mid] == complement:
    #                 # Found it! Return 1-based indices
    #                 return [i + 1, mid + 1]
    #             elif numbers[mid] < complement:
    #                 # Complement is larger, search right half
    #                 left = mid + 1
    #             else:
    #                 # Complement is smaller, search left half
    #                 right = mid - 1
                    
    #     return []

        
# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Amazon: 11
# - Google: 7
# - Meta: 5
# - TCS: 3
# - Microsoft: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Bloomberg: 4
# - Oracle: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Apple: 6
# - JPMorgan Chase: 2
# - Infosys: 2
# - Adobe: 2
# - EPAM Systems: 2
# - TikTok: 2
# - Zoho: 2
# - Visa: 2
# - Yandex: 2
# =================================================      