class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di={}
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                return True
        return False
        