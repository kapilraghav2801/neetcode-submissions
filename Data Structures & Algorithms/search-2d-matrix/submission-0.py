class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = (rows * cols) - 1

        while start <= end:
            mid = start + (end-start) //2 

            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True

            elif mid_val < target:
                start = mid + 1

            else:
                end = mid - 1

        return False

        # i = 0
        # j = cols - 1

        # while i < rows and j >= 0:
        #     if matrix[i][j] == target:
        #         return True

        #     elif matrix[i][j] > target:
        #         j -= 1
                
        #     else:
        #         i += 1

        # return False

        






# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Microsoft: 6
# - Amazon: 5
# - Google: 3
# - Meta: 2
# - Goldman Sachs: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - SAP: 3
# - Bloomberg: 2
# - TCS: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Oracle: 6
# - Adobe: 4
# - TikTok: 4
# - Apple: 3
# - Nutanix: 3
# - Walmart Labs: 2
# - DE Shaw: 2
# - Yandex: 2
# - PayPal: 2
# - Wissen Technology: 2
# =================================================
        