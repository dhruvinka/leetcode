class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                x=int(stack.pop())
                y=int(stack.pop())

                if i == '+':
                    stack.append(y+x)
                elif i == '-':
                    stack.append(y-x)
                elif i == '*':
                    stack.append(y*x)
                else :
                    stack.append(y/x)
        return stack[-1]
        



        