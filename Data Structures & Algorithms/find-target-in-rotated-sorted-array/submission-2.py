class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count=0
        for i in nums:
            if target not in nums:
                return -1
            else:
                if target == i:
                    return count
                count+=1
