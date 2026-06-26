class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        z=str(n)
        for i in z:
            if i == '1':
                c+=1
        return c
        