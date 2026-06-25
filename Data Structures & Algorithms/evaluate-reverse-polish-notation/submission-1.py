class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                x=stack.pop()
                y=stack.pop()

                if i == '+':
                    stack.append(x+y)
                elif i == '-':
                    stack.append(x-y)
                elif i == '*':
                    stack.append(x*y)
                else :
                    stack.append(x//y)
        return stack.pop()
        



        