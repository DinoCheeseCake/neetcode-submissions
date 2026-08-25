class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_l, row_r = 0, len(matrix)-1

        while row_l <= row_r:
            mid = (row_l + row_r) // 2
            if target > matrix[mid][0]:
                row_l = mid + 1
            elif target < matrix[mid][0]:
                row_r = mid - 1
            else:
                return True

        row = row_l = row_r

        col_l, col_r = 0, len(matrix[0])-1

        while col_l <= col_r:
            mid = (col_l + col_r) // 2
            if target > matrix[row][mid]:
                col_l = mid + 1
            elif target < matrix[row][mid]:
                col_r = mid - 1
            else:
                return True

        return False
