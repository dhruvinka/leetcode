class MinStack:

    def __init__(self):
        self.stack=[]
        self.Minval=None
        

    def push(self, val: int) -> None:
        if self.Minval is None:
            self.Minval=val
        else:
            self.Minval=min(self.Minval,val)

        self.stack.append((self.Minval,val))

        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        else:
            if self.stack:
                self.stack.pop()
            if self.stack:
                self.Minval=self.stack[-1][0]
            else:
                self.Minval = None
            
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        else:
            return self.stack[len(self.stack)-1][1]
        

    def getMin(self) -> int:
         if len(self.stack) == 0:
            return
         else:
            return self.stack[len(self.stack)-1][0]
        
