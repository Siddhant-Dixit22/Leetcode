class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L_mat, R_mat = 0, len(matrix) - 1

        while L_mat <= R_mat:
            M_mat = (L_mat + R_mat) // 2

            if (target > max(matrix[M_mat])):
                L_mat = M_mat + 1
            elif (target < min(matrix[M_mat])):
                R_mat = M_mat - 1
            else:
                L, R = 0, len(matrix[M_mat]) - 1
                while L <= R:
                    M = (L + R) // 2
                    if (matrix[M_mat][M] > target):
                        R = M - 1
                    elif (matrix[M_mat][M] < target):
                        L = M + 1
                    else:
                        return True
                return False
        
        return False