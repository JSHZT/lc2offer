class MinStack(object):

    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, x):
        self.items.append(x)
        if self.min_items == [] or self.min_items[-1] >= x:
            self.min_items.append(x)


    def pop(self):
        a = self.items.pop()
        if a == self.min_items[-1]:
            self.min_items.pop()
        return a

    def top(self):
        return self.items[-1] if self.items else None


    def min(self):
        return self.min_items[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
