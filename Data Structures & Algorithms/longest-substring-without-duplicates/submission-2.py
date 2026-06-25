class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=[]
        z=[]
        for i in range(len(s)):
            y=1
            z.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] in z:
                    break
                else:
                    print(s[i],s[j],end="->")
                    y+=1
                    z.append(s[j])
            x.append(y)
            z=[]
             
        y=max(x)
        return y
        