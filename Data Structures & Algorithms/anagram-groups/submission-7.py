class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        x={}
        for i in strs:
            xy="".join(sorted(i))
            if xy not in x:
                x[xy]=[i]
            else:
                x[xy].append(i)
        
        return list(x.values())