class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def print(self):
        print("Contents of stack(Right is top) are: ")
        for i in self.items:
            print(i, end=' ')
        print()

if __name__=='__main__':
    stack = Stack()
    stack.push(2)
    stack.push(5)
    stack.push(4)
    stack.print()
    print("Peeked element: " + str(stack.peek()))
    print("Popped element: " + str(stack.pop()))
    print("Popped element: " + str(stack.pop()))
    stack.print()
