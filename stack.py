from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def print(self):
        return(self.container)

me = Stack()
me.push(12)
me.push(11)
me.push(10)
print(me.peek())
me.pop()
print(me.is_empty())
print(me.size())
print(me.print())
