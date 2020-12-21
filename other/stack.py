class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        temp = len(self.stack) -1
        return self.stack[temp]

    def isEmpty(self):
        if(len(self.stack)==0):
            return True
        else:
            return False

    def size(self):
        return len(self.stack)