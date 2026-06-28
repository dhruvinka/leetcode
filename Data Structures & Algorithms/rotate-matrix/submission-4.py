class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        transpose = []
        for i in range(len(matrix[0])):
            row=[]
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transpose.append(row)
        for i in range(len(matrix[0])):
                matrix[i]=transpose[i][::-1]
           
        


       

       

        