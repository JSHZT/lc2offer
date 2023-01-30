class stack(object):
    
    def __init__(self):
        self.items = []
        
    def pop(self):
        return None if self.is_empty() else self.items.pop()
    
    def push(self, item):
        self.items.append(item)
        
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
    
class CQueue(object):

    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()

    def appendTail(self, value):
        while self.stack1.size() > 0:
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while self.stack2.size() > 0:
            self.stack1.push(self.stack2.pop())
        return

    def deleteHead(self):
        return -1 if self.stack1.is_empty() else self.stack1.pop()




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
