class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            curr_max = max(self.stack[-1][1], x)
            self.stack.append((x, curr_max))

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        MaxNum = self.stack[-1][1]
        arr = []

        while self.stack[-1][0] != MaxNum:
            arr.append(self.pop())
        
        self.pop()

        while arr:
            self.push(arr.pop())

        return MaxNum


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
