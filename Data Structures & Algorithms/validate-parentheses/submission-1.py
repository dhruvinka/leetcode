class Solution:
    def isValid(self, s: str) -> bool:
        
        # while '()' in s or '{}' in s or '[]' in s:
        #     s=s.replace('()','')
        #     s=s.replace('{}','')
        #     s=s.replace('[]','')
        # return s == ''

        stack=[]
        di={
            "}":"{",
            "]":"[",
            ")":"("
        }

        for i in s:
            if i not in di:
                stack.append(i)
            else:
                if not stack:
                    return False
                x=stack.pop()
                if di[i] != x:
                    return False
        
        if stack:
            return False
        return True
         

        