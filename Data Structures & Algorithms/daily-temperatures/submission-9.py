class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(len(temperatures)):
            count=0
            for j in range(i+1,len(temperatures)):
                if temperatures[i] > temperatures[j]:
                    # print(temperatures[i],i,j)
                    count+=1
            res.append(count)
        return res
        