class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        row=[0]*len(matrix)
        col=[0]*len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    row[i]=1
                    col[i]=1

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if row[i] == 1:
                    matrix[i][j]=0
                if col[j] == 1:
                    matrix[i][j]=0

            
        return matrix