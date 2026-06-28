class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrix[j][i]=matrix[i][j]

        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
            

       

        