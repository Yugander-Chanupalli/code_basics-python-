from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,elements):
        if self.is_empty():
            for i in elements:
                self.container.append(i)
    def is_empty(self):
        return len(self.container) == 0
    def pop(self):
        ls=['{', '}', '(', ')', '[', ']']
        print(self.container)
        ele=self.container.pop()
        print(ele)
        flag=False
        for i in ls:
            if i==ele:
                flag=True
                break
        print(flag)
stack=Stack()
stack.push("({a+b})")
stack.pop()
stack.push("[a+b]*(x+2y)*{gg+kk}")
stack.pop()
            

