class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        x=[]
        for i in s:
            x=s.count(i)
            if i not in x:
                x.append(x+k)
        return max(x)
        
        