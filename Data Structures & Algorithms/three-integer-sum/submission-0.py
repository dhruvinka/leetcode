class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()


        x=set()
        for i in range(len(nums)):
            a=nums[i]
            l=i+1
            r=len(nums)-1

            while l < r:
                if a +nums[l] +nums[r] == 0:
                    x.add((a,nums[l],nums[r]))
                    l+=1
                    r-=1
                elif a +nums[l] +nums[r] < 0:
                    l+=1
                else:
                    r-=1

        return [list(t) for t in x]
                   
                
                

