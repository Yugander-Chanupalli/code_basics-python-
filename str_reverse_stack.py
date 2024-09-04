from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,string):
        if len(string)>0:
            for i in string:
                self.container.append(i)
    def pop(self):
        reversed=""
        if self.is_empty():
            print("Empty")
        else:
            le=len(self.container)
            while le>0:
                reversed+=self.container.pop()
                le-=1
        return reversed
    def is_empty(self):
        return len(self.container)==0
            
    
stack=Stack()
stack.push("We will conquere COVID-19")
result=stack.pop()
print(result)