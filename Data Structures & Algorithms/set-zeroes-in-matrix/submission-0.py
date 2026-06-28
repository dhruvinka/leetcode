class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

      x=[(0,0)]*len(matrix)

      for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                x[i]=(i,j)
      for i in range(len(matrix)):
        for j in range(len(matrix)):
            if x[i][0] == 1:
                x[i][j]=0
            
            if x[i][1]==1:
                x[i][j]=0
      return matrix

      
       

        
        