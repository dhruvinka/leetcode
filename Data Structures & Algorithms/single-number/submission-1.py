class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=set()
        for i in nums:
            if i in x:
                x.remove()
            else:
                x.add()
            
        return list(x)

