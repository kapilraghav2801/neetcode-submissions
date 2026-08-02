class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # nums_s = sorted(nums)

        # left = 0
        # right = n - 1

        # while left < right:
        #     c_s = nums[left] + nums[right]

        #     if c_s == target:
        #         return [left, right]

        #     elif c_s > target:
        #         right -= 1

        #     else:
        #         left += 1


            
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment], i]

            seen[num] = i
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        