class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        for i in nums:
            co=nums.count(i)
            if i not in x:
                x[i]=co

        z=sorted(x.items(),key=lambda x:x[1],reverse=True)
        ans = []

        for key, value in z[:k]:
            ans.append(key)

        return ans

        