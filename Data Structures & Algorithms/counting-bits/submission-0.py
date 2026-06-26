class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in n:
           z= bin(i).count('1')
           res.append(z)
        return res

        