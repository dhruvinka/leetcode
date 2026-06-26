class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=set()
        for i in nums:
            if i in x:
                x.remove(i)
            else:
                x.add(i)
        z=list(x)
        return z

