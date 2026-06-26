class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        n=str(n)
        for i in n:
            if i == "1":
                c+=1
        return c
        