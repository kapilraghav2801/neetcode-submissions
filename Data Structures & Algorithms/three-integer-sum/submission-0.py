class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array so we can use two pointers
        nums.sort()

        n = len(nums)
        result = []

        # Pick one number at a time
        for i in range(n):

            # Skip duplicate first elements
            # Example:
            # [-4, -1, -1, 0, 1, 2]
            # We only process the first -1.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            left = i + 1
            right = n - 1

            while left < right:

                current_sum = nums[left] + nums[right]

                if current_sum == target:

                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left
                    # Example:
                    # [-2, 0, 0, 0, 2]
                    # After using the first 0, skip the remaining 0's.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right
                    # Example:
                    # [-2, 0, 2, 2, 2]
                    # After using the first 2, skip the remaining 2's.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    # Need a larger sum
                    left += 1

                else:
                    # Need a smaller sum
                    right -= 1

        return result

        # n = len(nums)
        # unique_triplets = set()

        # nums.sort()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 unique_triplets.add((nums[i],nums[j],nums[k]))

        # return [list(triplets) for triplets in unique_triplets]
# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 39
# - Amazon: 28
# - Microsoft: 10
# - Meta: 8
# - Bloomberg: 8
# - TCS: 4
# - Quince: 4
# - Infosys: 2
# - Apple: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Goldman Sachs: 3
# - Wissen Technology: 3
# - Walmart Labs: 2
# - Tesla: 2
# - Cisco: 2
# - Visa: 2
# - Accenture: 2
# - eBay: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - TikTok: 18
# - Oracle: 11
# - Cloudflare: 11
# - IBM: 5
# - Zoho: 5
# - Agoda: 5
# - Qualcomm: 4
# - SingleStore: 4
# - JPMorgan Chase: 3
# - Deloitte: 3
# =================================================   