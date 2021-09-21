#1886. Determine Whether Matrix Can Be Obtained By Rotation
#Given two n x n binary matrices mat and target, return true if it is possible to make mat 
#equal to target by rotating mat in 90-degree increments, or false otherwise.

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        result = [0,0,0,0]
        n = len(mat)
        for row_idx in range(0,n):
            if mat[row_idx] == target[row_idx]:
                result[0] += 1 
            if mat[row_idx] == [target[n-1-row_idx][i] for i in range(n-1,-1,-1)]:
                result[1] += 1
            if mat[row_idx] == [target[i][row_idx] for i in range(n-1,-1,-1)]:
                result[2] += 1
            if mat[row_idx] == [target[i][n-1 - row_idx] for i in range(0,n)]:
                result[3] += 1
        return True if n in result else False
		

"""
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        result = [0,0,0,0]
        n = len(mat)
        for rotate in range(0,4):
            mat = [[mat[i][j] for i in range(n-1,-1,-1)]for j in range(0,n)]
            if mat == target:
                return True
        return False
"""