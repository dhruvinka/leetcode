class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in nums:
            i^=i
        return nums
        