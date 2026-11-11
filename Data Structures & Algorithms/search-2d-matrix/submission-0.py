class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixOne = sum(matrix, [])

        if target in matrixOne:
            return True
        return False
        