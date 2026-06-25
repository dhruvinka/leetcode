class MinStack:

    def __init__(self):
        self.stack=[]
        self.Minval=0
        

    def push(self, val: int) -> None:
        if self.Minval == 0:
            self.Minval=val
        else:
            self.Minval=min(self.Minval,val)

        self.stack.append((self.Minval,val))

        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        else:
            self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        else:
            return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
         if len(self.stack) == 0:
            return
         else:
            return self.stack[len(self.stack)-1][0]
        
