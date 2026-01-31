class MinStack:

    def __init__(self):
        # cannot directly assign self = deque
        self.st = deque()

    def push(self, val: int) -> None:
        # we push a tuple with the (num, curr_min)
        if not self.st:
            curr_min = val
        else:
            curr_min = self.getMin()
        
        self.st.append((val,min(curr_min, val)))
        

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()