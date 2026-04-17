class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
        else:
            curr_max = max(x, self.stack[-1][1])
            self.stack.append((x, curr_max))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max_num = self.stack[-1][1]
        arr = []

        while self.stack[-1][0] != max_num:
            arr.append(self.pop())
        
        self.pop()

        while arr:
            self.push(arr.pop())
        return max_num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
