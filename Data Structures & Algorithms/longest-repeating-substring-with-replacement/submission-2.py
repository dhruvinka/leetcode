class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        di={}
        for i in s:
            x=s.count(i)
            if i not in di:
                di[i]=x+k
        return max(di)
            
        