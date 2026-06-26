class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # x=set()
        # for i in nums:
        #     if i in x:
        #         x.remove(i)
        #     else:
        #         x.add(i)
        
        # return list(x)[0]

        xor=0
        for i in nums:
            xor^=i
        return xor

